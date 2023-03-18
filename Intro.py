# basic imports
import asyncio
import streamlit as st
import pandas as pd

from apiclient import discovery
from google_auth_oauthlib.flow import Flow

import os
from streamlit_elements import Elements

# # The code below is for the layout of the page
# if "widen" not in st.session_state:
#     layout = "centered"
# else:
#     layout = "wide" if st.session_state.widen else "centered"

# st.set_page_config(
#     layout=layout, page_title="Google Search Console Connector", page_icon="🔌"
# )

# st.sidebar.image("logo.png", width=290)

st.sidebar.markdown("")

st.write("")

clientId = st.secrets['GOOGLE_CLIENT_ID']
clientSecret = st.secrets['GOOGLE_CLIENT_SECRET']
redirectUri = st.secrets['REDIRECT_URI']

st.markdown("")

# if "my_token_input" not in st.session_state:
#     st.session_state["my_token_input"] = ""

# if "my_token_received" not in st.session_state:
#     st.session_state["my_token_received"] = False

#     def charly_form_callback():
#         # st.write(st.session_state.my_token_input)
#         st.session_state.my_token_received = True
#         code = st.experimental_get_query_params()["code"][0]
#         st.session_state.my_token_input = code

#     with st.sidebar.form(key="my_form"):

st.markdown("")

mt = Elements()

def login():
    st.write("tried to log in")
            # st.write(st.session_state.my_token_input)
    #st.session_state.my_token_received = True
    code = st.experimental_get_query_params()["code"][0]
      #  st.session_state.my_token_input = code

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
#     + "&scope=https://www.googleapis.com/auth/webmasters.readonly&access_type=offline&prompt=consent",
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
