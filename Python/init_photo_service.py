import os
from Google import Create_Service

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'Python\client_secret_813529199477-2n2nj162fjogo0hh255mig1kkbjv1pmr.apps.googleusercontent.com.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME, API_VERSION, SCOPES)          