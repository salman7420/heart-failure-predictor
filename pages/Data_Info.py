# data_info_page.py
import streamlit as st
import pandas as pd

def show():
    st.title("📊 Data Information")
    st.markdown("""
    This page provides detailed information about all the clinical features used in our heart disease prediction model.
    Understanding these features is crucial for interpreting the predictions.
    """)
    
    # Create two tabs for Input and Output features
    tab1, tab2 = st.tabs(["📥 Input Features", "📤 Output Feature"])
    
    with tab1:
        st.header("Input Features (Clinical Parameters)")
        st.markdown("These are the patient characteristics used to make predictions.")
        
        # Input features data
        input_features = [
            {
                'Feature': 'age',
                'Description': 'Age of the patient',
                'Impact': 'Older age is generally associated with higher risk of heart disease',
                'Values': 'Numerical value (in years)',
                'Range': '29-77 years'
            },
            {
                'Feature': 'sex',
                'Description': 'Biological sex of the patient',
                'Impact': 'Gender can influence heart disease risk patterns',
                'Values': '0 = Female, 1 = Male',
                'Range': 'Binary (0 or 1)'
            },
            {
                'Feature': 'cp',
                'Description': 'Chest pain type',
                'Impact': 'Different types of chest pain indicate varying levels of cardiac risk',
                'Values': '0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic',
                'Range': '0-3'
            },
            {
                'Feature': 'trestbps',
                'Description': 'Resting blood pressure',
                'Impact': 'Higher blood pressure increases strain on the heart',
                'Values': 'Numerical value (mm Hg)',
                'Range': '94-200 mm Hg'
            },
            {
                'Feature': 'chol',
                'Description': 'Serum cholesterol level',
                'Impact': 'High cholesterol can lead to artery blockage and heart disease',
                'Values': 'Numerical value (mg/dl)',
                'Range': '126-564 mg/dl'
            },
            {
                'Feature': 'fbs',
                'Description': 'Fasting blood sugar',
                'Impact': 'High blood sugar is associated with diabetes and increased heart disease risk',
                'Values': '0 = False (≤120 mg/dl), 1 = True (>120 mg/dl)',
                'Range': 'Binary (0 or 1)'
            },
            {
                'Feature': 'restecg',
                'Description': 'Resting electrocardiographic results',
                'Impact': 'Abnormal ECG patterns can indicate heart problems',
                'Values': '0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy',
                'Range': '0-2'
            },
            {
                'Feature': 'thalach',
                'Description': 'Maximum heart rate achieved',
                'Impact': 'Lower maximum heart rate may indicate reduced cardiac capacity',
                'Values': 'Numerical value (beats per minute)',
                'Range': '71-202 bpm'
            },
            {
                'Feature': 'exang',
                'Description': 'Exercise induced angina',
                'Impact': 'Chest pain during exercise is a strong indicator of heart disease',
                'Values': '0 = No, 1 = Yes',
                'Range': 'Binary (0 or 1)'
            },
            {
                'Feature': 'oldpeak',
                'Description': 'ST depression induced by exercise relative to rest',
                'Impact': 'Higher values indicate more significant ECG changes during stress',
                'Values': 'Numerical value',
                'Range': '0.0-6.2'
            },
            {
                'Feature': 'slope',
                'Description': 'Slope of the peak exercise ST segment',
                'Impact': 'Specific slope patterns can indicate coronary artery disease',
                'Values': '0: Upsloping, 1: Flat, 2: Downsloping',
                'Range': '0-2'
            },
            {
                'Feature': 'ca',
                'Description': 'Number of major vessels colored by fluoroscopy',
                'Impact': 'More blocked vessels indicate more severe coronary artery disease',
                'Values': 'Numerical value (0-3)',
                'Range': '0-3'
            },
            {
                'Feature': 'thal',
                'Description': 'Thalassemia (blood disorder) measurement',
                'Impact': 'Specific patterns can indicate blood flow issues to the heart',
                'Values': '1: Normal, 2: Fixed defect, 3: Reversible defect',
                'Range': '1-3'
            }
        ]
        
        # Create DataFrame and display
        df_input = pd.DataFrame(input_features)
        st.dataframe(
            df_input,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Feature": st.column_config.TextColumn("Feature", width="small"),
                "Description": st.column_config.TextColumn("Description", width="medium"),
                "Impact": st.column_config.TextColumn("Impact on Prediction", width="large"),
                "Values": st.column_config.TextColumn("Values & Meaning", width="large"),
                "Range": st.column_config.TextColumn("Typical Range", width="small")
            }
        )
    
    with tab2:
        st.header("Output Feature (Prediction Target)")
        st.markdown("This is what our model predicts based on the input features.")
        
        # Output feature data
        output_features = [
            {
                'Feature': 'target',
                'Description': 'Presence of heart disease',
                'Impact': 'The main outcome we want to predict',
                'Values': '0 = No heart disease, 1 = Heart disease present',
                'Range': 'Binary (0 or 1)'
            }
        ]
        
        # Create DataFrame and display
        df_output = pd.DataFrame(output_features)
        st.dataframe(
            df_output,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Feature": st.column_config.TextColumn("Feature", width="small"),
                "Description": st.column_config.TextColumn("Description", width="medium"),
                "Impact": st.column_config.TextColumn("Impact on Prediction", width="large"),
                "Values": st.column_config.TextColumn("Values & Meaning", width="large"),
                "Range": st.column_config.TextColumn("Typical Range", width="small")
            }
        )
        
        # Add some explanatory notes
        st.info("""
        **💡 Clinical Notes:**
        - A prediction of **1** means the model detected signs of heart disease
        - A prediction of **0** means no significant signs were detected
        - This prediction should be used as a screening tool, not a definitive diagnosis
        - Always consult healthcare professionals for medical decisions
        """)
    
    # Add some summary statistics
    st.markdown("---")
    st.subheader("📈 Dataset Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Features", "14")
    
    with col2:
        st.metric("Input Features", "13")
    
    with col3:
        st.metric("Output Feature", "1")
    
    # Quick reference guide
    st.markdown("---")
    st.subheader("🎯 Quick Reference Guide")
    
    st.markdown("""
    **Most Important Predictive Features:**
    - `thalach`: Maximum heart rate achieved (lower = higher risk)
    - `exang`: Exercise-induced angina (presence = higher risk)  
    - `cp`: Chest pain type (asymptomatic = higher risk)
    - `oldpeak`: ST depression (higher = higher risk)
    - `ca`: Number of blocked vessels (more = higher risk)
    """)
    
    # Clinical significance section
    st.markdown("---")
    st.subheader("🏥 Clinical Significance")
    
    st.markdown("""
    **Why these features matter:**
    
    - **Demographic factors** (age, sex) help establish baseline risk profiles
    - **Vital signs** (blood pressure, cholesterol) indicate cardiovascular health
    - **Exercise test results** (thalach, exang, oldpeak) reveal how the heart performs under stress
    - **Imaging results** (ca, thal) provide direct evidence of coronary artery disease
    
    Our model combines these diverse clinical indicators to provide a comprehensive risk assessment.
    """)

if __name__ == "__main__":
    show()