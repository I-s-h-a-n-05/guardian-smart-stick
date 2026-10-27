import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Guardian | Smart Stick Monitor",
    page_icon="🛡️",
    layout="wide",
)

# Hide Streamlit default chrome so the dashboard fills the full page
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

html_file = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1000, scrolling=True)
