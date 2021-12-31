from init_photo_service import service
import pandas as pd

"""
list method
"""
response = service.albums().list(
    pageSize=50,
    excludeNonAppCreatedData=False
).execute()

lstAlbums = response.get('albums')
#nextPageToken = response.get('nextPageToken')