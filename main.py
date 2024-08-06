import time
from datetime import datetime
import ollama
from stravalib.client import Client
import pickle
import os
import sys

script_location = os.path.dirname(os.path.abspath(sys.argv[0]))
client = Client()
MY_STRAVA_CLIENT_ID, MY_STRAVA_CLIENT_SECRET = open(script_location + '/client.secret').read().strip().split(',')

MY_STRAVA_CLIENT_ID = MY_STRAVA_CLIENT_ID.strip()
MY_STRAVA_CLIENT_SECRET = MY_STRAVA_CLIENT_SECRET.strip()

# url = client.authorization_url(client_id=MY_STRAVA_CLIENT_ID, redirect_uri='http://127.0.0.1:5000/authorization',
#                                scope=['read_all', 'profile:read_all', 'activity:read_all', 'profile:write',
#                                       'activity:write'])
# print(url)
#
# CODE = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
#
# access_token = client.exchange_code_for_token(client_id=xxxxx,
#                                               client_secret="xxxxxxxxxxxxxxx", code=CODE)
# with open('./access_token.pickle', 'wb') as f:
#     pickle.dump(access_token, f)


with open(script_location + '/access_token.pickle', 'rb') as f:
    access_token = pickle.load(f)


def check_token():
    global access_token
    if time.time() > access_token['expires_at']:
        print('Token has expired, will refresh')

        refresh_response = client.refresh_access_token(client_id=int(MY_STRAVA_CLIENT_ID),
                                                       client_secret=str(MY_STRAVA_CLIENT_SECRET),
                                                       refresh_token=access_token['refresh_token'])
        access_token = refresh_response
        with open(script_location + '/access_token.pickle', 'wb') as f:
            pickle.dump(refresh_response, f)
        print('Refreshed token saved to file')
        client.access_token = refresh_response['access_token']
        client.refresh_token = refresh_response['refresh_token']
        client.token_expires_at = refresh_response['expires_at']

    else:
        print('Token still valid, expires at {}'
              .format(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(access_token['expires_at']))))
        client.access_token = access_token['access_token']
        client.refresh_token = access_token['refresh_token']
        client.token_expires_at = access_token['expires_at']


check_token()

# Get all activities
activities = client.get_activities()
print('Activities:')

count = 0
for a in activities:
    activity = client.get_activity(a.id)
    print(activity.name)
    day = activity.start_date.day
    month = activity.start_date.month
    year = activity.start_date.year
    daysSince = (datetime.now().date() - activity.start_date.date()).days

    if (activity.description is not None and activity.description != "") or daysSince > 5:
        break

    response = ollama.chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': 'Provide only an original quote that inspires reflection about nature, thought, or the essence of life. '
                       'Avoid using logic-based expressions like true or false. Do not provide any context or explanation. Do not '
                       'attribute the quote to any author or source. Do not use quotation marks.'

        },
    ])
    print(response["message"]["content"])
    client.update_activity(activity.id,
                           description=response["message"]["content"] + "\n\n-llama3.1   \n" + datetime.now()
                           .strftime("%Y-%m-%d %H:%M:%S"))
