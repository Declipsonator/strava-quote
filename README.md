# Strava Quotes

## Info
Sets the description of all of your activities within five days (or until your last one with a description) to a generated llama3.1 quote. Sometimes some beautiful things come out 😄

<img alt="strava activity with description: Life is not a series of beginnings and endings, but an endless stream of moments in which we find ourselves being who we are." src="https://github.com/user-attachments/assets/d82b421c-3619-4cad-910e-5e14b88aa23a" width="500px" />


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
## Credits
Independently developed by [Jackson Hickey](https://github.com/declipsonator). Licensed under the GNU General Public License v3.0.
