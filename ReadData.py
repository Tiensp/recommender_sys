import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('firebase_key/service_account_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

