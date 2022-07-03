#!/usr/bin/python3

from dotenv import load_dotenv
from datetime import datetime
from time import sleep
import requests
import os
import pandas as pd
import numpy as np
import json

load_dotenv()



test_mode = True

#credentials
if test_mode == True:
    app_id = os.getenv('sandbox_app_id')
    access_token = os.getenv('sandbox_access_token')
else:
    app_id = os.getenv('prod_app_id')
    access_token = os.getenv('prod_access_token')

def get_oauth_token():
    if test_mode == True:
        oauth_token = os.getenv('test_account_access_token')
    else:
        print('need more code')


app_name = os.getenv('app_name')
redirect_url = os.getenv('redirect_url')



honey_db = sqlalchemy.create_engine(os.getenv('honey_db'))
api_base_url = 'https://connect.squareup.com/v2'



def list_bookings(ACCESS_TOKEN):
    headers = {
    'Square-Version': '2022-06-16',
    'Authorization': ACCESS_TOKEN,
    'Content-Type': 'application/json'
    }
    url = f'{api_base_url}/bookings'
    response = requests.get(url=url, headers=headers)
    data = response.json()
    return data

