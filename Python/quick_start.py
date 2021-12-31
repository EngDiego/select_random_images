# pip install google-auth-oauthlib requests

import json
import pickle
import os.path

import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

cliente_secret_json = 'Python\client_secret_813529199477-2n2nj162fjogo0hh255mig1kkbjv1pmr.apps.googleusercontent.com.json'
token='Python\capable-avatar-332112-b68229503722.json'
token_pickle = 'Python\token.pickle'


ALBUM_ID = 'Esposa'

from os.path import join, dirname
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
SCOPES = 'https://www.googleapis.com/auth/photoslibrary.readonly'

store = file.Storage(join(dirname(__file__), token_pickle))
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(join(dirname(__file__), 'cliente_secret_json', SCOPES))
    creds = tools.run_flow(flow, store)
google_photos = build('photoslibrary', 'v1', http=creds.authorize(Http()))

day, month, year = ('0', '6', '2019')  # Day or month may be 0 => full month resp. year
date_filter = [{"day": day, "month": month, "year": year}]  # No leading zeroes for day an month!
nextpagetoken = 'Dummy'
while nextpagetoken != '':
    nextpagetoken = '' if nextpagetoken == 'Dummy' else nextpagetoken
    results = google_photos.mediaItems().search(
            body={"filters":  {"dateFilter": {"dates": [{"day": day, "month": month, "year": year}]}},
                  "pageSize": 10, "pageToken": nextpagetoken}).execute()
    # The default number of media items to return at a time is 25. The maximum pageSize is 100.
    items = results.get('mediaItems', [])
    nextpagetoken = results.get('nextPageToken', '')
    for item in items:
            print(f"{item['filename']} {item['mimeType']} '{item.get('description', '- -')}'"
                      f" {item['mediaMetadata']['creationTime']}\nURL: {item['productUrl']}")