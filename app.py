import requests
import streamlit.components.v1 as components

url = "https://raw.githubusercontent.com/Keshava199-web/Portfolio/main/portfolio.html"
html = requests.get(url).text

components.html(html, height=1000, scrolling=True)
