import os
import json
import pickle
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
from flask import Flask, redirect, render_template, flash, request, jsonify, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required, logout_user, login_user, LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from groq import Groq 

# --- App Configuration ---
app = Flask(__name__, 
            static_url_path='', 
            static_folder='static', 
            template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "tandrima"

# --- Groq Configuration (NEW KEY UPDATED) ---
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# --- Load Machine Learning Model ---
try:
    model = pickle.load(open('stresslevel.pkl', 'rb'))
except Exception as e:
    print(f"⚠️ Stress model file not found: {e}")
    model = None

# --- Database Model ---
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(20), unique=True)
    pas = db.Column(db.String(1000))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Authentication Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        usn = request.form.get('usn')
        pas = request.form.get('pas')
        if User.query.filter_by(usn=usn).first():
            flash("UserID is already taken", "warning")
            return render_template("usersignup.html")
        new_user = User(usn=usn, pas=generate_password_hash(pas))
        db.session.add(new_user)
        db.session.commit()
        return render_template("userlogin.html")
    return render_template("usersignup.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        usn, pas = request.form.get('usn'), request.form.get('pas')
        user = User.query.filter_by(usn=usn).first()
        if user and check_password_hash(user.pas, pas):
            login_user(user)
            return redirect(url_for('home'))
        flash("Invalid Credentials", "danger")
    return render_template("userlogin.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- Feature Routes ---
@app.route('/music')
@login_required
def music(): return render_template('music.html')

@app.route('/quizandgame')
@login_required
def quizandgame(): return render_template('quizandgame.html')

@app.route('/exercises')
@login_required
def exercises(): return render_template('exercises.html')

@app.route('/analysis')
@login_required
def analysis():
    try:
        train_df = pd.read_csv('dreaddit-train.csv', encoding='ISO-8859-1')
        fig = px.pie(train_df, names='subreddit', title='Subreddit Distribution')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('analysis.html', graphJSON=graphJSON)
    except:
        return "Analysis data not found."

# --- CHAT ROUTE (Fixed 302 and AI logic) ---
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'reply': 'Empty message.'})

        # Safety Check
        if any(word in user_message.lower() for word in ['suicide', 'kill']):
            return jsonify({'reply': "Please contact 988 Crisis Line immediately."})

        # Groq Call
        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are MindEase, a supportive mental health assistant. Give short responses."},
                    {"role": "user", "content": user_message}
                ]
            )
            reply = completion.choices[0].message.content
            return jsonify({'reply': reply})
        except Exception as api_err:
            print(f"API Error: {api_err}")
            return jsonify({'reply': "Connection failed. Please check your internet or API key."})

    except Exception as e:
        return jsonify({'reply': "System error. Please try again."})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)