# TikTok Analyzer and Recommendation App

## 🌟 Vision
Build the #1 AI-powered TikTok app that helps creators grow and monetize their brand faster, ethically, and impactfully.

---

## 🎯 Purpose
Help TikTok creators grow faster by showing them what to post next — based on trends, engagement patterns, and their audience.

---

## 🧠 Core Features

### 1. 🔮 Content Recommendation Engine
- Predicts which video types (funny, dance, educational, etc.) are likely to perform well.
- Considers user profile: age, location, goals.
- Analyzes past video engagement (manually entered or scraped in future).

### 2. 📈 Engagement Forecast
- Predicts likes, views, and shares using a trained ML model.
- Shows confidence level in performance for each idea.

### 3. 🔥 Hashtag & Trend Advisor (Phase 2)
- Suggests relevant trending hashtags for each video idea.
- Option to sync trends using TikTok discovery or 3rd-party API.

### 4. 🗕️ Smart Video Planner
- Recommends content themes and best times to post for the next 7 to 30 days.
- Option to customize by goal: grow followers, promote brand, go viral.

---

## ✨ Bonus Features (Future Phases)
- AI Caption Writer / Title Generator
- “Grow Like This Creator” feature (find similar successful TikTokers)
- Trend tracker: monitor popular sounds and hashtags
- Mental wellness: daily motivational quote or burnout check-in
- Music and sound recommender based on trending audio
- Sponsorship predictor: brands likely to align with creator profile

---

## 🧪 Backend (Model Requirements)
- Model input: video type, user profile, time, music, tags
- Output: engagement score, ranking, suggestions
- Built with logistic regression or small neural net for prediction

**Sample Python model logic (Phase 1 prototype):**
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Simulated training data
training_data = pd.DataFrame({
    'age': [22, 25, 30, 21, 35],
    'location_CA': [0, 1, 0, 1, 0],
    'location_NY': [1, 0, 0, 0, 1],
    'location_TX': [0, 0, 1, 0, 0],
    'tag_funny': [1, 0, 0, 1, 0],
    'tag_dance': [0, 1, 0, 0, 0],
    'tag_educational': [0, 0, 1, 0, 0],
    'music_genre_pop': [1, 0, 0, 1, 0],
    'music_genre_none': [0, 0, 1, 0, 1],
    'creator_popularity': [0.9, 0.75, 0.6, 0.85, 0.5],
    'engaged': [1, 0, 1, 0, 1]
})

# Prepare features and model
X = training_data.drop(columns='engaged')
y = training_data['engaged']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = LogisticRegression()
model.fit(X_scaled, y)

# Sample user input for prediction
new_idea = pd.DataFrame([{
    'age': 24,
    'location_CA': 0,
    'location_NY': 1,
    'location_TX': 0,
    'tag_funny': 1,
    'tag_dance': 0,
    'tag_educational': 0,
    'music_genre_pop': 1,
    'music_genre_none': 0,
    'creator_popularity': 0.8
}])

new_idea_scaled = scaler.transform(new_idea)
pred = model.predict_proba(new_idea_scaled)[0][1]
print("Predicted Engagement Probability:", round(pred, 2))
```

---

## 🎨 UI Plan

### Phase 1: Web Form Interface (Prototype)
- **Frontend (Streamlit):**
  - Input Fields:
    - Age (dropdown or number input)
    - Location (dropdown: CA, NY, TX)
    - Video type (checkboxes: funny, dance, educational)
    - Music genre (dropdown or multiselect: pop, none, hiphop, etc.)
    - Creator popularity (slider: 0.0–1.0)
  - Submit button: “Generate Recommendation”

- **Output Display:**
  - Engagement Probability (with a progress bar or color indicator)
  - Suggestion summary (e.g., "Funny video with pop music is likely to perform well.")
  - Top 3 trend tags to consider (placeholder phase 2)

---

## ✅ Phase 1 Deliverables (MVP)
- Working recommendation script (based on age, location, tags, music)
- Streamlit frontend interface
- Basic printable 7-day video posting plan
- `requirements.txt` for easy install and GitHub deployment

---

## 📦 Files to Upload to GitHub

### `app.py`
```python
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Simulated training data
training_data = pd.DataFrame({
    'age': [22, 25, 30, 21, 35],
    'location_CA': [0, 1, 0, 1, 0],
    'location_NY': [1, 0, 0, 0, 1],
    'location_TX': [0, 0, 1, 0, 0],
    'tag_funny': [1, 0, 0, 1, 0],
    'tag_dance': [0, 1, 0, 0, 0],
    'tag_educational': [0, 0, 1, 0, 0],
    'music_genre_pop': [1, 0, 0, 1, 0],
    'music_genre_none': [0, 0, 1, 0, 1],
    'creator_popularity': [0.9, 0.75, 0.6, 0.85, 0.5],
    'engaged': [1, 0, 1, 0, 1]
})

X = training_data.drop(columns='engaged')
y = training_data['engaged']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = LogisticRegression()
model.fit(X_scaled, y)

st.title("TikTok Engagement Recommender")
age = st.slider("Age", 13, 60, 24)
location = st.selectbox("Location", ["CA", "NY", "TX"])
video_type = st.multiselect("Video Type", ["funny", "dance", "educational"])
music = st.selectbox("Music Genre", ["pop", "none"])
popularity = st.slider("Creator Popularity", 0.0, 1.0, 0.8)

if st.button("Generate Recommendation"):
    input_dict = {
        'age': age,
        'location_CA': 1 if location == "CA" else 0,
        'location_NY': 1 if location == "NY" else 0,
        'location_TX': 1 if location == "TX" else 0,
        'tag_funny': 1 if "funny" in video_type else 0,
        'tag_dance': 1 if "dance" in video_type else 0,
        'tag_educational': 1 if "educational" in video_type else 0,
        'music_genre_pop': 1 if music == "pop" else 0,
        'music_genre_none': 1 if music == "none" else 0,
        'creator_popularity': popularity
    }
    df = pd.DataFrame([input_dict])
    scaled = scaler.transform(df)
    prob = model.predict_proba(scaled)[0][1]
    st.success(f"Engagement Probability: {round(prob * 100)}%")
```

### `requirements.txt`
```
streamlit
pandas
scikit-learn
```

> Next: Upload these two files to your GitHub repo under the `tiktok-recommender` project.
