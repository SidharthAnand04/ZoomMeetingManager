import os
from zoomus import ZoomClient
from dotenv import load_dotenv
import re


load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
EMAIL_ADDRESS = os.getenv('USER_EMAIL')

client = ZoomClient(API_KEY, API_SECRET)
response = client.user.get(id=EMAIL_ADDRESS)

if response.status_code == 200:
    print('API Credentials are valid')
else:
    print('API Credentials are invalid')

regex_start_time = r"[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}"

in_msg = input('enter time')
if re.search(regex_start_time, in_msg):
    print('pass')
else:
    print('fail')