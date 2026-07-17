import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="Smart Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# LOAD MODEL 
model = joblib.load("model.pkl")

#  CROP MAPPING 
crop_dict = {
    1: "Rice 🌾 (ধান)",
    2: "Maize 🌽 (ভুট্টা)",
    3: "Chickpea 🫘 (ছোলা)",
    4: "Kidney Beans 🫘 (রাজমা)",
    5: "Pigeon Peas 🌱 (অড়হর ডাল)",
    6: "Moth Beans 🌿 (মথ শিম)",
    7: "Mung Bean 🌱 (মুগ ডাল)",
    8: "Black Gram ⚫ (মাষকলাই)",
    9: "Lentil 🥣 (মসুর ডাল)",
    10: "Pomegranate 🍎 (ডালিম)",
    11: "Banana 🍌 (কলা)",
    12: "Mango 🥭 (আম)",
    13: "Grapes 🍇 (আঙুর)",
    14: "Watermelon 🍉 (তরমুজ)",
    15: "Muskmelon 🍈 (বাঙ্গি)",
    16: "Apple 🍏 (আপেল)",
    17: "Orange 🍊 (কমলা)",
    18: "Papaya 🥭 (পেঁপে)",
    19: "Coconut 🥥 (নারিকেল)",
    20: "Cotton ☁️ (তুলা)",
    21: "Jute 🌾 (পাট)",
    22: "Coffee ☕ (কফি)"
}
#  CUSTOM CSS 
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#134E5E,#71B280);
}

.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:white;
}

.subtitle{
    text-align:center;
    font-size:22px;
    color:#F5F5F5;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    background:linear-gradient(90deg,#1B5E20,#43A047);
    color:white;
    font-size:22px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.03);
}

.result-card{
    background:linear-gradient(135deg,#1B5E20,#43A047);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0px 8px 25px rgba(0,0,0,0.2);
}

.footer{
    text-align:center;
    color:white;
    font-size:15px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR 
with st.sidebar:

    st.title("🌾 Crop AI Dashboard")

    st.success("22 Crop Categories")
    st.success("Random Forest Classifier")
    st.success("AI Powered Recommendation")
    st.success("Instant Prediction")

    st.markdown("---")

    st.subheader("📌 About Project")

    st.write("""
This project recommends the most suitable crop based on:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- Soil pH
- Rainfall
""")

    st.markdown("---")

    st.subheader("🤖 Model Information")
    st.write("Algorithm: Random Forest")
    st.write("Input Features: 7")
    st.write("Output Classes: 22")

#  HEADER 
st.markdown(
    '<div class="main-title">🌱 Smart Crop Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Agriculture Assistant for Modern Farming</div>',
    unsafe_allow_html=True
)

st.write("")

#  INPUT 
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌾 Soil Parameters")

    N = st.number_input("Nitrogen (N)", 0.0, 200.0, 90.0)
    P = st.number_input("Phosphorus (P)", 0.0, 200.0, 42.0)
    K = st.number_input("Potassium (K)", 0.0, 200.0, 43.0)
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)

with col2:
    st.subheader("☁️ Weather Parameters")

    temperature = st.number_input("Temperature (°C)", -10.0, 60.0, 25.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 80.0)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0, 150.0)

st.write("")

#  PREDICTION 
if st.button("🚀 Recommend Best Crop"):

    input_data = pd.DataFrame(
        [[N,P,K,temperature,humidity,ph,rainfall]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(input_data)[0]

    crop_name = crop_dict.get(int(prediction), str(prediction))

    try:
        confidence = max(model.predict_proba(input_data)[0]) * 100
    except:
        confidence = 100

    st.markdown(
        f"""
        <div class="result-card">
        <h1>🌾 Recommended Crop</h1>
        <h1>{crop_name}</h1>
        <h3>🎯 Confidence Score: {confidence:.2f}%</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(confidence/100)

#INPUT SUMMARY 
    st.subheader("📋 Input Summary")

    summary = pd.DataFrame({
        "Feature":[
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "pH",
            "Rainfall"
        ],
        "Value":[
            N,P,K,temperature,humidity,ph,rainfall
        ]
    })

    st.dataframe(summary,use_container_width=True)

# BANGLA EXPLANATION
    st.subheader("🇧🇩 কেন এই ফসলটি নির্বাচন করা হয়েছে?")

    st.success(f"""
   মাটির NPK মান {crop_name} চাষের জন্য উপযুক্ত।

   বর্তমান তাপমাত্রা এবং আর্দ্রতা এই ফসলের বৃদ্ধির জন্য ভালো।

   বৃষ্টিপাতের পরিমাণ গ্রহণযোগ্য সীমার মধ্যে রয়েছে।

   মাটির pH এই ফসলের জন্য উপযোগী।

   AI মডেল বিশ্লেষণ করে সর্বোচ্চ সম্ভাবনা হিসেবে {crop_name} নির্বাচন করেছে।
""")
    
# ENGLISH EXPLANATION 
    st.subheader("🇬🇧 Why was this crop selected?")

    st.info(f"""
✅ Soil nutrient values are suitable for {crop_name}.

✅ Temperature and humidity are within the ideal growing range.

✅ Rainfall conditions are favorable.

✅ Soil pH supports healthy growth.

✅ The AI model predicted {crop_name} with the highest probability.
""")
# TIPS 
    tips = {
        "Rice 🌾":"💧 Requires high water availability and irrigation.",
        "Maize 🌽":"☀️ Prefers warm weather and moderate rainfall.",
        "Banana 🍌":"🌴 Thrives in humid tropical environments.",
        "Mango 🥭":"🌞 Requires plenty of sunlight and warm temperatures.",
        "Cotton ☁️":"🌤️ Performs best in warm climates.",
        "Coffee ☕":"⛰️ Grows best in cooler climates with rainfall."
    }

    if crop_name in tips:
        st.warning(tips[crop_name])

# FEATURE IMPORTANCE 
    try:
        st.subheader("📊 Feature Importance")

        importance = model.feature_importances_

        fig, ax = plt.subplots(figsize=(8,5))

        ax.bar(
            ["N","P","K","Temp","Humidity","pH","Rainfall"],
            importance
        )

        ax.set_title("Feature Importance")
        ax.set_ylabel("Importance Score")

        st.pyplot(fig)

    except:
        pass

#  FOOTER 
st.markdown("""
<div class="footer">
<hr>
🌱 Smart Crop Recommendation System <br>
Built with Streamlit & Machine Learning <br><br>
👨‍💻 Developed by Dipto Howlader Prethul
</div>
""", unsafe_allow_html=True)