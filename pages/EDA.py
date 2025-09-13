# pages/EDA.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show():
    st.title("📈 Exploratory Data Analysis")
    
    st.markdown("""
    This section provides interactive visualizations to explore the heart disease dataset
    and understand relationships between different features.
    """)
    
    # Load data
    @st.cache_data
    def load_data():
        try:
            df = pd.read_csv('heart-disease.csv')
            return df
        except FileNotFoundError:
            st.error("heart-disease.csv file not found. Please make sure it's in the same directory.")
            return pd.DataFrame()
    
    df = load_data()
    
    if df.empty:
        st.stop()
    
    # Preprocess data for better visualization
    df_processed = df.copy()
    df_processed['sex'] = df_processed['sex'].map({0: 'Female', 1: 'Male'})
    df_processed['target'] = df_processed['target'].map({0: 'No Disease', 1: 'Heart Disease'})
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs([
        "Target Distribution", 
        "Feature Analysis", 
        "Correlation Matrix",
        "Interactive Plots"
    ])
    
    with tab1:
        st.subheader("Target Variable Distribution")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            target_counts = df_processed['target'].value_counts()
            fig = px.pie(
                values=target_counts.values, 
                names=target_counts.index,
                title='Distribution of Heart Disease Cases'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Bar chart by gender
            gender_target = pd.crosstab(df_processed['sex'], df_processed['target'])
            fig = px.bar(
                gender_target, 
                barmode='group',
                title='Heart Disease Cases by Gender'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Age distribution by target
        st.subheader("Age Distribution by Heart Disease Status")
        fig = px.histogram(
            df_processed, 
            x='age', 
            color='target',
            marginal='box',
            nbins=30,
            title='Age Distribution by Heart Disease Status'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Feature Distributions")
        
        feature = st.selectbox(
            "Select a feature to visualize:",
            options=[col for col in df.columns if col not in ['target', 'sex']]
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if df[feature].dtype in ['int64', 'float64']:
                fig = px.histogram(
                    df_processed, 
                    x=feature, 
                    color='target',
                    marginal='box',
                    title=f'Distribution of {feature}'
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig = px.histogram(
                    df_processed, 
                    x=feature, 
                    color='target',
                    title=f'Distribution of {feature}'
                )
                st.plotly_chart(fig, use_container_width=True)
                
        with col2:
            st.subheader(f"Summary Statistics for {feature}")
            if df[feature].dtype in ['int64', 'float64']:
                st.dataframe(df[feature].describe())
            else:
                st.dataframe(df_processed[feature].value_counts())
    
    with tab3:
        st.subheader("Correlation Matrix")
        
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        corr_matrix = df[numeric_cols].corr()
        
        fig = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            title='Correlation Matrix of Numerical Features'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Top Features Correlated with Heart Disease")
        target_corr = corr_matrix['target'].drop('target').sort_values(ascending=False)
        target_corr_df = pd.DataFrame({
            'Feature': target_corr.index,
            'Correlation with Target': target_corr.values
        })
        st.dataframe(target_corr_df)
    
    with tab4:
        st.subheader("Interactive Feature Relationships")
        
        col1, col2 = st.columns(2)
        
        with col1:
            x_feature = st.selectbox(
                "Select X-axis feature:",
                options=[col for col in df.columns if col != 'target'],
                index=0
            )
        
        with col2:
            y_feature = st.selectbox(
                "Select Y-axis feature:",
                options=[col for col in df.columns if col != 'target'],
                index=3
            )
        
        color_by = st.selectbox(
            "Color by:",
            options=['target', 'sex'],
            index=0
        )
        
        fig = px.scatter(
            df_processed,
            x=x_feature,
            y=y_feature,
            color=color_by,
            title=f'{y_feature} vs {x_feature}',
            hover_data=['age']
        )
        st.plotly_chart(fig, use_container_width=True)