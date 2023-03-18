# basic imports
import asyncio
import streamlit as st
import pandas as pd
from apiclient import discovery
from google_auth_oauthlib.flow import Flow
import os
import json
from streamlit_elements import Elements
import requests
# from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

state = st.session_state
state.logged_in = False

clientId = st.secrets['GOOGLE_CLIENT_ID']
clientSecret = st.secrets['GOOGLE_CLIENT_SECRET']
redirectUri = st.secrets['REDIRECT_URI']

# # The code below is for the layout of the page
# if "widen" not in st.session_state:
#     layout = "centered"
# else:
#     layout = "wide" if st.session_state.widen else "centered"

# st.set_page_config(
#     layout=layout, page_title="Google Search Console Connector", page_icon="🔌"
# )

mt = Elements()

@st.cache_resource
def get_email():
    code = st.experimental_get_query_params()["code"][0]

    # Get access token
    url="https://accounts.google.com/o/oauth2/token"
    body = {
        "code": code,
        "grant_type": "authorization_code",
        "client_id": clientId,
        "client_secret": clientSecret,
        "redirect_uri": redirectUri,
    }
    r = requests.post(url, json=body)
    response = json.loads(r.content)
    state.access_token = response['access_token']
    state.refresh_token = response['refresh_token']
    state.id_token = response['id_token']

    # Get current user's email address
    url = "https://www.googleapis.com/oauth2/v3/userinfo?client_id="+clientId+"&client_secret="+clientSecret+"&redirect_uri="+redirectUri+"&scope=https://www.googleapis.com/auth/userinfo.email&access_type=offline&prompt=consent"
    r = requests.get(url,params={'access_token': state.access_token})
    response = json.loads(r.content)
    state.email = response['email']
    logged_in_msg = "You're currently logged in as "+state.email
    st.success(logged_in_msg, icon="✅")

def check_if_logged_in():
    if st.experimental_get_query_params():
        state.logged_in = True
    else:
        state.logged_in = False


def sidebar():
#     css=f'''
#     [data-testid="stSidebarNav"] {{
#         position:absolute;
#         bottom: 0;
#         z-index: 1;
#     }}
#     [data-testid="stSidebarNav"] > ul {{
#         padding-top: 2rem;
#     }}
#     [data-testid="stSidebarNav"] > div {{
#         position:absolute;
#         top: 0;
#     }}
#     [data-testid="stSidebarNav"] > div > svg {{
#         transform: rotate(180deg) !important;
#     }}
#     [data-testid="stSidebarNav"] + div {{
#         overflow: scroll;
#         max-height: 66vh;
#     }}
#     '''

#     st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.image("Logo.png")

#         st.image("Logo.png", width=290)
        check_if_logged_in()
        if not state.logged_in:
            mt.button(
                "Log in with Google",
                target="_blank",
                size="large",
                variant="contained",
    #             start_icon=mt.icons.exit_to_app,
                onclick="login()",
                style={"color": "#FFFFFF", "background": "#FF4B4B", "text-transform": "unset !important";},
                href="https://accounts.google.com/o/oauth2/auth?response_type=code&client_id="
                + clientId
                + "&redirect_uri="
                + redirectUri
                + "&scope=https://www.googleapis.com/auth/userinfo.email&access_type=offline&prompt=consent",
            )
            
#             mt.button(
#                 "Log in with Google",
#                 target="_blank",
#                 size="large",
#                 variant="contained",
#     #             start_icon=mt.icons.exit_to_app,
#                 onclick="login()",
#                 style={"color": "#FFFFFF", "background": "#FF4B4B"},
#                 href="https://accounts.google.com/o/oauth2/auth?response_type=code&client_id="
#                 + clientId
#                 + "&redirect_uri="
#                 + redirectUri
#                 + "&scope=https://www.googleapis.com/auth/userinfo.email&access_type=offline&prompt=consent",
#             )

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
        else:
            get_email()
            
sidebar()
