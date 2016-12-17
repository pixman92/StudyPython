import requests
r = requests.get('https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=1307263279337637&client_secret=641f789bf2dd634bd822c9ec330c8b35')
access_token = r.text.split('=')[1]
print r.[0]
