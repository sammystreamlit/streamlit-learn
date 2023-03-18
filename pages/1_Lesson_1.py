import streamlit as st
import time
import numpy as np
from pathlib import Path

state=st.session_state

with st.sidebar:
    if state.logged_in and state.email:
        st.write("You're currently logged in as "+state.email)
    else:
    if not state.logged_in:
        mt.button(
            "Sign-in with Google",
            target="_blank",
            size="large",
            variant="contained",
            start_icon=mt.icons.exit_to_app,
            onclick="login()",
            style={"color": "#FFFFFF", "background": "#FF4B4B"},
            href="https://accounts.google.com/o/oauth2/auth?response_type=code&client_id="
            + clientId
            + "&redirect_uri="
            + redirectUri
            + "&scope=https://www.googleapis.com/auth/userinfo.email&access_type=offline&prompt=consent",

        )

        mt.show(key="687")

        credentials = {
            "installed": {
                "client_id": clientId,
                "client_secret": clientSecret,
                "redirect_uris": redirectUri,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://accounts.google.com/o/oauth2/token",
            }
        }

        flow = Flow.from_client_config(
            credentials,
            scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
            redirect_uri=redirectUri,
        )

        auth_url, _ = flow.authorization_url(prompt="consent")


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

intro_markdown = read_markdown_file("pages/installation.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

