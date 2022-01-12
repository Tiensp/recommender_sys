import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('firebase_key/service_account_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Get Data from firebase
def getHotelsData():
    hotels = list(db.collection(u'hotels').stream())

    hotels_dict = list(map(lambda x: x.to_dict(), hotels))
    df = pd.DataFrame(hotels_dict)

    df['ratingCount'] = df['ratingList'].str.len()      # Create new feature Rating Count
    # Drop unuseful feature
    df.drop(columns=['thumbnail', 'img', 'detailInfo', 'ratingList', 'utilities'], axis=1, inplace=True)
    #print(df.info())
    return df

def getRatingData():
    ratings = list(db.collection(u'rating').stream())

    ratings_dict = list(map(lambda x: x.to_dict(), ratings))
    df = pd.DataFrame(ratings_dict)

    # Drop unuseful feature
    df.drop(columns=['thumbnail', 'img', 'detailInfo', 'ratingList', 'utilities'], axis=1, inplace=True)
    #print(df.info())
    return df

def getFakeRating():
    df = pd.read_json('data/ratings.json')
    return df
