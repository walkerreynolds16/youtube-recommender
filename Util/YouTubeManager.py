import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_authenticated_service(): # Modified
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret.json"

    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
        credentials = tools.run_flow(flow, store)
    return googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
