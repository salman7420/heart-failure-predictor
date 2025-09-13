# pages/Home.py
import streamlit as st

def show():
    # Main header with fancy styling
    st.markdown('<h1 class="main-header">❤️ Heart Failure Prediction System</h1>', unsafe_allow_html=True)
    
    # Project introduction card
    st.markdown("""
    <div class="project-card">
        <h2>Revolutionizing Cardiac Care with AI</h2>
        <p>An advanced machine learning system that predicts heart failure risk with accuracy using clinical data. 
        Our platform leverages state-of-the-art algorithms to provide early warnings and support clinical decision-making.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Team section
    st.markdown("## 👥 Our Team")
    st.markdown("---")
    
    # Create columns for team members
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
        <div class="team-card">
            <h3>Member 1</h3>
            <p>Salman Rasheed</p>
            
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <h3>Member 2</h3>
            <p>Zakwan Jaleel</p>
            
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="team-card">
            <h3>Member 3</h3>
            <p>Yousef Alkhalifa</p>
            
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="team-card">
            <h3>Member 4</h3>
            <p>Ahmad</p>
            
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="team-card">
            <h3>Member 5</h3>
            <p>Younes</p>
            
        </div>
        """, unsafe_allow_html=True)
    
    # Features section
    st.markdown("## 🚀 Key Features")
    st.markdown("---")
    
    features_col1, features_col2, features_col3 = st.columns(3)
    
    with features_col1:
        st.info("""
        **🤖 Multiple AI Models**  
        Choose from 3 powerful algorithms:  
        • Logistic Regression  
        • Random Forest  
        • K-Nearest Neighbors
        """)
    
    with features_col2:
        st.success("""
        **📊 Comprehensive Analysis**  
        Detailed EDA with interactive  
        visualizations and data insights  
        for better understanding
        """)
    
    with features_col3:
        st.warning("""
        **🎯 Accurate Predictions**  
        Accurate in predicting  
        heart failure risk based on  
        clinical parameters
        """)
    
    # How to use section
   

if __name__ == "__main__":
    show()