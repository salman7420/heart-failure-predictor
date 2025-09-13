# app.py
import streamlit as st

# Page configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="Heart Failure Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        color: #ff4b4b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .team-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .project-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar navigation
    st.sidebar.title("❤️ Navigation")
    st.sidebar.markdown("---")
    
    # Page selection
    page = st.sidebar.radio("Select a page:", 
                           ["🏠 Home", "📊 Data Information", "📈 EDA & Findings", "❤️ Heart Failure Predictor"])
    
    # Load the selected page
    if page == "🏠 Home":
        import pages.Home as home_page
        home_page.show()
    elif page == "📊 Data Information":
        import pages.Data_Info as data_info_page
        data_info_page.show()
    elif page == "📈 EDA & Findings":
        import pages.EDA as eda_page
        eda_page.show()
    elif page == "❤️ Heart Failure Predictor":
        import pages.Predictor as predictor_page
        predictor_page.show()

if __name__ == "__main__":
    main()