import streamlit as st

# Read HTML file
with open("portfolio.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display HTML inside Streamlit
st.components.v1.html(html_content, height=900, scrolling=True)
