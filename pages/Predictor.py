# predictor_page.py
import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the saved models with caching
@st.cache_resource
def load_models():
    models = {}
    try:
        with open('Data/logistic_regression_model.pkl', 'rb') as file:
            models['Logistic Regression'] = pickle.load(file)
        with open('Data/random_forest_model.pkl', 'rb') as file:
            models['Random Forest'] = pickle.load(file)
        with open('Data/knn_model.pkl', 'rb') as file:
            models['K-Nearest Neighbors'] = pickle.load(file)
    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}")
    return models

def show():
    st.title("❤️ Heart Disease Risk Assessment")
    st.markdown("Complete the form below to analyze your heart disease risk using advanced AI models.")
    
    # Create a form for user input with better spacing
    with st.form("heart_disease_form"):
        
        # Personal Information Section
        st.header("👤 Personal Information")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.slider(
                "**Age**",
                min_value=20,
                max_value=100,
                value=50,
                help="Age of the patient in years"
            )
        
        with col2:
            sex = st.selectbox(
                "**Gender**",
                options=[0, 1],
                format_func=lambda x: "Female" if x == 0 else "Male",
                help="0 = Female, 1 = Male"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)  # Add space
        
        # Medical Measurements Section
        st.header("🩺 Medical Measurements")
        st.markdown("---")
        
        col3, col4 = st.columns(2)
        
        with col3:
            cp = st.selectbox(
                "**Chest Pain Type**",
                options=[0, 1, 2, 3],
                format_func=lambda x: {
                    0: "Typical Angina",
                    1: "Atypical Angina", 
                    2: "Non-anginal Pain",
                    3: "Asymptomatic"
                }[x],
                help="Type of chest pain experienced"
            )
            
            trestbps = st.slider(
                "**Resting Blood Pressure** (mm Hg)",
                min_value=90,
                max_value=200,
                value=120,
                help="Resting blood pressure measurement"
            )
            
            chol = st.slider(
                "**Cholesterol Level** (mg/dl)",
                min_value=100,
                max_value=600,
                value=250,
                help="Serum cholesterol level"
            )
        
        with col4:
            fbs = st.selectbox(
                "**Fasting Blood Sugar** > 120 mg/dl",
                options=[0, 1],
                format_func=lambda x: "No (≤120 mg/dl)" if x == 0 else "Yes (>120 mg/dl)",
                help="Fasting blood sugar level"
            )
            
            restecg = st.selectbox(
                "**Resting ECG Results**",
                options=[0, 1, 2],
                format_func=lambda x: {
                    0: "Normal",
                    1: "ST-T Wave Abnormality",
                    2: "Left Ventricular Hypertrophy"
                }[x],
                help="Resting electrocardiographic results"
            )
            
            thalach = st.slider(
                "**Max Heart Rate Achieved**",
                min_value=70,
                max_value=220,
                value=150,
                help="Maximum heart rate during exercise"
            )
        
        st.markdown("<br><br>", unsafe_allow_html=True)  # Add more space
        
        # Exercise Test Results Section
        st.header("🏃‍♂️ Exercise Test Results")
        st.markdown("---")
        
        col5, col6 = st.columns(2)
        
        with col5:
            exang = st.selectbox(
                "**Exercise-Induced Angina**",
                options=[0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Chest pain during exercise"
            )
            
            oldpeak = st.slider(
                "**ST Depression** (Oldpeak)",
                min_value=0.0,
                max_value=6.2,
                value=1.0,
                step=0.1,
                help="ST depression induced by exercise"
            )
        
        with col6:
            slope = st.selectbox(
                "**Slope of ST Segment**",
                options=[0, 1, 2],
                format_func=lambda x: {
                    0: "Upsloping",
                    1: "Flat", 
                    2: "Downsloping"
                }[x],
                help="Slope of peak exercise ST segment"
            )
            
            ca = st.slider(
                "**Number of Major Vessels**",
                min_value=0,
                max_value=3,
                value=1,
                help="Number of major vessels colored by fluoroscopy (0-3)"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)  # Add space
        
        # Additional Information Section
        st.header("📋 Additional Information")
        st.markdown("---")
        
        thal = st.selectbox(
            "**Thalassemia Result**",
            options=[1, 2, 3],
            format_func=lambda x: {
                1: "Normal",
                2: "Fixed Defect",
                3: "Reversible Defect"
            }[x],
            help="Thalassemia test results"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)  # Add space
        
        # Submit button for the form
        col_submit, _ = st.columns([1, 3])
        with col_submit:
            submitted = st.form_submit_button("💾 Save Information", use_container_width=True)
        
        if submitted:
            st.success("✅ Patient information saved successfully! Now select a model to predict.")
    
    st.markdown("<br>", unsafe_allow_html=True)  # Space between form and prediction buttons
    
    # Load models
    models = load_models()
    
    # Prediction buttons section
    st.header("🔍 Make Prediction")
    st.markdown("Select one or more models to analyze your heart disease risk:")
    
    # Create columns for prediction buttons with better spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    col7, col8, col9, col10 = st.columns(4)
    
    predictions = {}
    
    with col7:
        if st.button("🤖 Logistic Regression", use_container_width=True, type="primary"):
            predictions['Logistic Regression'] = make_prediction(models['Logistic Regression'], 
                                                               age, sex, cp, trestbps, chol, fbs, 
                                                               restecg, thalach, exang, oldpeak, 
                                                               slope, ca, thal)
    
    with col8:
        if st.button("🌲 Random Forest", use_container_width=True, type="primary"):
            predictions['Random Forest'] = make_prediction(models['Random Forest'], 
                                                         age, sex, cp, trestbps, chol, fbs, 
                                                         restecg, thalach, exang, oldpeak, 
                                                         slope, ca, thal)
    
    with col9:
        if st.button("📏 K-Nearest Neighbors", use_container_width=True, type="primary"):
            predictions['K-Nearest Neighbors'] = make_prediction(models['K-Nearest Neighbors'], 
                                                               age, sex, cp, trestbps, chol, fbs, 
                                                               restecg, thalach, exang, oldpeak, 
                                                               slope, ca, thal)
    
    with col10:
        if st.button("🎯 All Models", use_container_width=True, type="secondary"):
            for model_name, model in models.items():
                predictions[model_name] = make_prediction(model, 
                                                         age, sex, cp, trestbps, chol, fbs, 
                                                         restecg, thalach, exang, oldpeak, 
                                                         slope, ca, thal)
    
    # Display predictions with better spacing
    if predictions:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.header("📊 Prediction Results")
        st.markdown("---")
        
        for model_name, (prediction, probability, confidence) in predictions.items():
            with st.container():
                st.markdown(f"### {model_name}")
                
                col11, col12 = st.columns([3, 1])
                
                with col11:
                    if prediction == 1:
                        st.error(f"**❤️ Heart Disease Detected**")
                        st.markdown(f"*Risk probability: {probability:.1%}*")
                    else:
                        st.success(f"**✅ No Heart Disease Detected**")
                        st.markdown(f"*Risk probability: {probability:.1%}*")
                
                with col12:
                    st.metric("Confidence", f"{confidence:.1%}")
                
                st.markdown("---")
        
        # Show overall consensus if multiple models were used
        if len(predictions) > 1:
            st.markdown("<br>", unsafe_allow_html=True)
            show_final_assessment(predictions)

def make_prediction(model, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    """Make prediction using the given model"""
    try:
        # Create input array in the correct order
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Get prediction probabilities
        prediction_proba = model.predict_proba(input_data)[0]
        
        # Get confidence (max probability)
        confidence = max(prediction_proba)
        
        # Get the probability of heart disease (class 1)
        heart_disease_prob = prediction_proba[1]
        
        return prediction, heart_disease_prob, confidence
        
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None, None, None

def show_final_assessment(predictions):
    """Show final assessment when multiple models are used"""
    st.subheader("🎯 Final Assessment")
    
    # Count predictions
    heart_disease_count = sum(1 for pred, _, _ in predictions.values() if pred == 1)
    no_disease_count = sum(1 for pred, _, _ in predictions.values() if pred == 0)
    
    # Calculate average probability
    avg_probability = np.mean([prob for _, prob, _ in predictions.values()])
    
    col13, col14 = st.columns(2)
    
    with col13:
        if heart_disease_count > no_disease_count:
            st.error("## ⚠️ Overall: High Risk of Heart Disease")
            st.markdown("""
            **Recommendations:**
            - Consult a cardiologist immediately
            - Schedule comprehensive cardiac testing
            - Monitor your symptoms closely
            - Consider lifestyle changes
            """)
        else:
            st.success("## ✅ Overall: Low Risk of Heart Disease")
            st.markdown("""
            **Recommendations:**
            - Maintain healthy lifestyle habits
            - Regular cardiovascular exercise
            - Balanced diet low in cholesterol
            - Annual health check-ups
            """)
    
    with col14:
        st.metric("Average Risk Probability", f"{avg_probability:.1%}")
        st.metric("Models Agreement", f"{heart_disease_count}/{len(predictions)} detected risk")
        
        st.info("""
        **💡 Important Note:**
        This prediction is for screening purposes only.
        Always consult healthcare professionals for
        proper medical diagnosis and treatment.
        """)

if __name__ == "__main__":
    show()