import streamlit as st
import time
import numpy as np
from pathlib import Path
from Intro import sidebar

state=st.session_state

sidebar()

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

intro_markdown = read_markdown_file("pages/installation.md")
st.markdown(intro_markdown, unsafe_allow_html=True)
