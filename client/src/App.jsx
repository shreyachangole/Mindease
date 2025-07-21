import React from 'react';
import Navbar from './components/nav'
import Feature from './components/feature'
import Footer from './components/footer'

function App() {
  return (
    <div>
      <Navbar />
      <main>
        <section className="hero text-center py-20 bg-gradient-to-r from-indigo-100 to-pink-100">
          <h1 className="text-4xl font-bold mb-4">Welcome to MindEase 🧠</h1>
          <p className="text-lg text-gray-700">
            Your mental well-being companion. Share your feelings, track your thoughts, and connect with supportive resources.
          </p>
        </section>

        <Feature />
      </main>
      <Footer />
    </div>
  );
}

export default App;
