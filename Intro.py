# basic imports
import asyncio
import streamlit as st
import pandas as pd
from apiclient import discovery
from google_auth_oauthlib.flow import Flow
import os
from streamlit_elements import Elements
import requests
# from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# from googleapiclient import discovery



# import google-api-python-client

# # The code below is for the layout of the page
# if "widen" not in st.session_state:
#     layout = "centered"
# else:
#     layout = "wide" if st.session_state.widen else "centered"

# st.set_page_config(
#     layout=layout, page_title="Google Search Console Connector", page_icon="🔌"
# )

mt = Elements()

clientId = st.secrets['GOOGLE_CLIENT_ID']
clientSecret = st.secrets['GOOGLE_CLIENT_SECRET']
redirectUri = st.secrets['REDIRECT_URI']

creds = {
    "installed": {
        "client_id": clientId,
        "client_secret": clientSecret,
        "redirect_uris": redirectUri,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
    }
}


# st.sidebar.image("logo.png", width=290)
button2 = st.button("get email")

if button2:
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
    access_token = st.experimental_get_query_params()["code"][0]
    credentials = Credentials(None, client_id=clientId, client_secret=clientSecret)
    #    url = "https://accounts.google.com/o/oauth2/auth?response_type=code&client_id="+clientId+"&redirect_uri="+redirectUri+"&scope=https://www.googleapis.com/auth/userinfo.email&access_type=offline&prompt=consent"
    
    # get access token
    url="https://accounts.google.com/o/oauth2/token&grant_type=authorization_code&client_id="+clientId+"&client_secret="+clientSecret+"&redirect_uri="+redirectUri
    r = requests.get(url)
    st.write(r.content)

#     url = "https://www.googleapis.com/oauth2/v3/userinfo?response_type=code&client_id="+clientId+"&client_secret="+clientSecret+"&redirect_uri="+redirectUri+"&scope=https://www.googleapis.com/auth/userinfo.email&access_type=offline&prompt=consent"
#     r = requests.get(url,params={'access_token': access_token})
#     st.write(r.status_code)
#     st.write(r.content)


    #     service = build('people', 'v1', credentials=credentials)
#     results = service.people().connections().list(
#         resourceName='people/me',
#         pageSize=10,
#         personFields='names,emailAddresses').execute()
#     connections = results.get('connections', [])

#     for person in connections:
#         names = person.get('names', [])
#         if names:
#             name = names[0].get('displayName')
#             st.write(name)
#     r = requests.get('https://www.googleapis.com/oauth2/v3/userinfo',params={'access_token': access_token, access_type:offline, prompt:consent})
#     st.write(r.json())
#     results = service.people()
#     connections = service.people().connections().list(resourceName='people/me', personFields='names').execute()
#     st.write(connections)
#     people = service.people().connections().list('people/me')

#     people = service.people().connections().list('people/me', personFields='names,emailAddresses')
#     st.write(people)


#     discovery.build("people", "v1", credentials = credentials)
    
#     credentials = google.oauth2.credentials.Credentials(
#         access_token,
# #         refresh_token = refresh_token,
#         token_uri = 'https://accounts.google.com/o/oauth2/token',
#         client_id = clientId,
#         client_secret = clientSecret
#     )


#     creds = None
 
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     people_service = build('people', 'v1', credentials=creds)

#     people = people_service.people().connections().list('people/me', personFields='names,emailAddresses')
    
#     authed_session = AuthorizedSession(credentials)
#     response = authed_session.get('https://www.googleapis.com/oauth2/v1/userinfo') 
#      except HttpError as err:
#         print(err)

    # try:
    #     service = build('people', 'v1', credentials=creds)

    #     # Call the People API
    #     print('List 10 connection names')
    #     results = service.people().connections().list(
    #         resourceName='people/me',
    #         pageSize=10,
    #         personFields='names,emailAddresses').execute()
    #     connections = results.get('connections', [])

    #     for person in connections:
    #         names = person.get('names', [])
    #         if names:
    #             name = names[0].get('displayName')
    #             print(name)
    # except HttpError as err:
    #     print(err)

st.sidebar.markdown("")
st.write("")

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

# st.markdown("")


# button = st.button("get email")
# if button:
# # def login():
#     st.write("tried to log in")
#             # st.write(st.session_state.my_token_input)
#     #st.session_state.my_token_received = True
#     code = st.experimental_get_query_params()["code"][0]
#       #  st.session_state.my_token_input = code
#     #     st.write(code)
# #     api_url = "https://www.googleapis.com/oauth2/v2/userinfo&access_token="
#     #api_url = "https://www.googleapis.com/drive/v3/about&access_token="
#     api_url="https://people.googleapis.com/v1/{resourceName=people/*}&personFields=emailAddresses&access_token="
#     api_url = api_url+code
#     response = requests.get(api_url)
#     st.write(response.content)
#     st.write(response.status_code)
#     st.write(response.json())
#     if response.status_code != 204:
#         st.write(response.json())
#     else: 
#         st.write(response)
#     st.write(response.json())

def get_user_info(credentials):
    """Send a request to the UserInfo API to retrieve the user's information.

    Args:
    credentials: oauth2client.client.OAuth2Credentials instance to authorize the
                 request.
    Returns:
    User information as a dict.
    """
    user_info_service = build(
      serviceName='oauth2', version='v2',
      http=credentials.authorize(httplib2.Http()))
    user_info = None
    try:
        user_info = user_info_service.userinfo().get().execute()
    except:
        logging.error('An error occurred')
    if user_info and user_info.get('id'):
        return user_info
    else:
        raise NoUserIdException()


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
#     + "&scope=https://www.googleapis.com/auth/drive&access_type=offline&prompt=consent",

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
