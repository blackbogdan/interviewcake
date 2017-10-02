__author__ = 'bkapusta'
client_id = '1ed4bdf6d630473fa600e549da0f658b'
client_secret = 'c05afa6142cf4fa3955dd5afb2c3c56b'
access_token1 = '5423293433.1ed4bdf.ef00531e9abb43459111076fd050f75a'
# oauth_url = 'https://api.instagram.com/oauth/access_token'
import requests
from pprint import pprint
oauth_url = 'https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri=http://127.0.0.1&response_type=token'.\
    format(client_id)
def authenticate():
    r = requests.get(oauth_url)
    with open("instagram_resp.html", "w") as f:
        f.write(r.text)
    print r.text
    # print r.json()
    print r.status_code
    # headers = {'client_id':client_id,
    #            'client_secret':client_secret,
    #            'grant_type':'authorization_code',
    # }

def get_media_id():

    url = 'http://api.instagram.com/oembed?url=https://www.instagram.com/p/BUqRMIil15e/'
    resp = requests.get(url)
    return resp.json()
def write_comment():
    url = 'https://api.instagram.com/v1/media/{}/comments'.format(get_media_id()['media_id'])
    headers ={
        'access_token':access_token1,
        'text':'Good pic, REST'
    }
    # curl -F 'access_token=ACCESS-TOKEN' \
    #  -F 'text=This+is+my+comment' \

    r = requests.post(url, data=headers)
    return r.json()


# client_id=CLIENT_ID' \
#     -F 'client_secret=CLIENT_SECRET' \
#     -F 'grant_type=authorization_code' \
#     -F 'redirect_uri=AUTHORIZATION_REDIRECT_URI' \
#     -F 'code=CODE' \

if __name__ == "__main__":
    # authenticate()
    print get_media_id()['media_id']
    print write_comment()