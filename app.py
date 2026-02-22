import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ---------- Load trained model ----------
model = joblib.load("ids_model.pkl")

# ---------- Page Title ----------
st.title("🔐 Intrusion Detection System")

# ---------- File Upload ----------
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    # ---------- Read Uploaded Data ----------
    data = pd.read_csv(uploaded_file)

    st.subheader("📂 Uploaded Data")
    st.write(data.head())

    # ---------- Prediction Button ----------
    if st.button("Predict"):

        # Make copy for processing
        processed_data = data.copy()

        # ---------- DROP LABEL COLUMN ----------
        if "labels" in processed_data.columns:
            processed_data = processed_data.drop("labels", axis=1)

            st.success("✅ Labels column removed successfully")

            # Show processed data
            st.subheader("⚙️ Processed Data (Used for Prediction)")
            st.write(processed_data.head())

        # ---------- ENCODE CATEGORICAL FEATURES ----------
        categorical_cols = ["protocol_type", "service", "flag"]

        for col in categorical_cols:
            if col in processed_data.columns:
                le = LabelEncoder()
                processed_data[col] = le.fit_transform(processed_data[col])

        # ---------- SCALE FEATURES ----------
        scaler = StandardScaler()
        processed_scaled = scaler.fit_transform(processed_data)

        # ---------- MODEL PREDICTION ----------
        predictions = model.predict(processed_scaled)

        # ---------- ADD PREDICTION TO ORIGINAL DATA ----------
        data["Prediction"] = ["🚨 Attack" if x else "✅ Normal" for x in predictions]

        # ---------- SHOW FINAL RESULTS ----------
        st.subheader("📊 Final Prediction Results")
        st.write(data)
