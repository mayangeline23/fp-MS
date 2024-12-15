import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Health Disease Prediction - Final Project", layout="centered")

# Custom CSS to set Times New Roman font and style the title and body text
st.markdown("""
    <style>
        /* Set Times New Roman font for all titles and markdown */
        body {
            font-family: 'Times New Roman', serif;
        }

        /* Title Styling */
        .title {
            font-family: 'Times New Roman', serif;
            font-size: 36px;
            font-weight: bold;  /* Makes the title bold */
            color: black;  /* Ensure it's visible on both light and dark themes */
            text-align: center;
            padding-bottom: 20px;
        }

        /* Paragraph Styling */
        .streamlit-expanderHeader, .streamlit-expanderContent {
            font-family: 'Times New Roman', serif;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Times New Roman', serif;
        }

        p {
            font-family: 'Times New Roman', serif;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Welcome Message 
st.markdown("""
    <p style="font-family: 'Times New Roman', serif; font-size: 50px;">
    Health Disease Prediction🩺
    </p>
    """, unsafe_allow_html=True)

# Introduction with custom styling for Times New Roman font
st.markdown("""
<p>
This project focuses on <strong>Health Disease</strong>, showcasing our application of modeling and simulation techniques. 
We've worked together to explore synthetic health data, perform statistical analysis, and develop predictive models to assess various health risks.
</p>

<p>
This project is the culmination of our group's dedication and effort for the <strong>CSEC 413 Modeling and Simulation</strong> course, and we're excited to share our work with you.
</p>
""", unsafe_allow_html=True)

# Why Health Disease Prediction with custom styling for Times New Roman font
st.markdown("""
<p>
💡 <strong>Why Health Disease Prediction?</strong>  
Health diseases continue to be a major concern globally. By leveraging data modeling and simulation, our aim is to provide insights that contribute to understanding and managing health risks effectively.
</p>
""", unsafe_allow_html=True)

# Thank you message with custom styling for Times New Roman font
st.markdown("""
<p>
Thank you for taking the time to view our work. Happy exploring! 🤓
</p>
""", unsafe_allow_html=True)
