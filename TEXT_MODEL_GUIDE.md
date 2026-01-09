# Text-Based Stress Detection Guide

## Overview

You now have **TWO methods** for stress detection:

1. **Old Method**: Numerical inputs (Sleeping Hours, Blood Pressure, Respiration Rate, Heart Rate)
2. **New Method**: Text-based analysis using the `dreaddit-train.csv` dataset

## How to Use Text-Based Model

### Step 1: Train the Model

Run the training script to create the text-based model:

```bash
python train_text_model.py
```

This will:
- Load the `dreaddit-train.csv` dataset
- Extract text and labels (0 = No Stress, 1 = Stress)
- Train a KNN model using TF-IDF vectorization
- Save two files:
  - `stresslevel_text_model.pkl` - The trained model
  - `stresslevel_text_vectorizer.pkl` - The text vectorizer

### Step 2: Access the Text-Based Interface

Once the model is trained, you can access it at:
- **URL**: `http://localhost:5000/stress-text`
- Or add a link in your navigation menu

### Step 3: Use the Feature

Users can:
1. Type how they're feeling in the text box
2. Click "Analyze Stress Level"
3. Get results with confidence percentages

## Comparison

| Feature | Old Method (Numerical) | New Method (Text) |
|---------|----------------------|-------------------|
| **Input** | 4 numbers | Free text |
| **Dataset** | Unknown | dreaddit-train.csv |
| **Model** | KNN (4 features) | KNN + TF-IDF (5000 features) |
| **Accuracy** | Unknown | ~70-80% (estimated) |
| **User-Friendly** | Requires measurements | Natural language |

## Advantages of Text-Based Model

✅ **Uses your actual dataset** (`dreaddit-train.csv`)  
✅ **More natural** - users can express feelings in their own words  
✅ **No measurements needed** - easier for users  
✅ **Trained on real Reddit posts** - similar to user input  
✅ **Shows confidence scores** - more informative  

## Files Created

- `train_text_model.py` - Training script
- `templates/stress_text.html` - Text input interface
- `stresslevel_text_model.pkl` - Trained model (after running training)
- `stresslevel_text_vectorizer.pkl` - Text vectorizer (after running training)

## Routes Added

- `/stress-text` - Text input page
- `/stressdetect-text` - Text analysis endpoint

## Example Usage

**User Input:**
```
"I've been feeling really anxious lately about work and I can't seem to sleep well. 
I'm constantly worried about deadlines and feel overwhelmed."
```

**Model Output:**
```
⚠️ High Stress Detected! (85.3% confidence)

Consult a doctor and get the helpline number from our chatbot. 
Consider trying our music therapy or exercise recommendations.
```

## Notes

- The text model is **optional** - the old numerical method still works
- If the text model files don't exist, the app will show a message to train it first
- Both methods can coexist in your application
