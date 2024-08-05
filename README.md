# Strava Quotes
## Installation:
### Step 1:
Follow the first section of [this tutorial](https://medium.com/analytics-vidhya/accessing-user-data-via-the-strava-api-using-stravalib-d5bee7fdde17).
### Step 2:
Download [Ollama](https://ollama.com/).\
Run `ollama run llama3.1`\
Run `ollama serve`

### Step 3:
Uncomment this code:
```python
url = client.authorization_url(client_id=MY_STRAVA_CLIENT_ID, redirect_uri='http://127.0.0.1:5000/authorization',
                               scope=['read_all', 'profile:read_all', 'activity:read_all', 'profile:write',
                                      'activity:write'])
print(url)

CODE = 'xxxxxxxxxxxxxxxxxxxxxxxxx'

access_token = client.exchange_code_for_token(client_id=xxxxx,
                                               client_secret="xxxxxxxxxxxxxxx", code=CODE)
with open('./access_token.pickle', 'wb') as f:
    pickle.dump(access_token, f)
```
Then run the program once, open the url and authorize.
After that, put in your id and secret and the code is in the tutorial.
### Step 4:
Comment out the code and you're good. I use crontab to run the program every hour.