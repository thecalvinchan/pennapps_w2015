import json
from flask import Flask, request, redirect, g, render_template, session, url_for, flash
from flask_oauth import OAuth
import requests
import base64
import json
import os
from playlist_result import find_playlist
from analysis import *

app = Flask(__name__, static_url_path="")
app.secret_key = 'Ab!??%/!jmN]LWX/,?RTasoidjfoiajs' 
oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='x9mme4cCpvf0ePlCEQkjLXwUw',
    consumer_secret='bA3mkQKsIlIE7HYBLu12TmnC7TNrPZ9OI88HReBN88holz2ivF'
)

@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

#Authorization code flow
url = "https://accounts.spotify.com/authorize"
CLIENT_ID = "29262729c4fa49afaf21f40f56feb5cf"
REDIRECT_URI = "http://127.0.0.1:8080/callback/q"
SCOPE = "user-modify-private user-modify-public"
CLIENT_SECRET = "25fcda1a3c154584905e996935cc68b8"

payload = {"client_id":CLIENT_ID, "response_type":"code",
           "redirect_uri":REDIRECT_URI, "scope":SCOPE}

@app.route('/')
def index():
    s_redirect = "https://accounts.spotify.com/authorize/?client_id=" +  \
    CLIENT_ID+ "&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3 \
    A8080%2Fcallback%2Fq&scope=playlist-modify-public+playlist-modify-private"
    return render_template("index.html",
        spotify_redirect=s_redirect,
        twitter_login=url_for('login')
    )

@app.route('/twitterlogin')
def login():
    if get_twitter_token():
        print get_twitter_token()
        return redirect(url_for('index'))
    return twitter.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    flash('You were signed in as %s' % resp['screen_name'])
    return redirect(next_url)

@app.route('/generate')
def generate():
    """Generates a spotify playlist given a twitter dataset"""
    tweets = ["having a great time at PENNAPPS today",
              "This is so cool, I love this place!"]
    result = get_playlist_type(tweets)
    playlist = find_playlist(result)

    return render_template("result.html", playlist=playlist )

@app.route("/callback/q")
def callback():
	access_token = request.args
	code_payload = {"grant_type":"authorization_code",
                    "code":str(access_token['code']),
                    "redirect_uri":REDIRECT_URI}
	base64encoded = base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET)

	headers = {"Authorization":"Basic %s" % base64encoded}
	post_request = requests.post("https://accounts.spotify.com/api/token",
        data=code_payload,headers=headers)
	json_response = json.loads(post_request.text)
	test_response = requests.get("https://api.spotify.com/v1/me",
        headers={'Authorization':'Bearer ' + json_response[u'access_token']})
	json_profile = json.loads(test_response.text)
	playlists = requests.get(json_profile['href']+"/playlists",
        headers={'Authorization':'Bearer '+json_response[u'access_token']})
	jsoned_playlists = json.loads(playlists.text)
	json_array = []
	for playlist in jsoned_playlists['items']:
		json_array.append(playlist)

	return render_template("index.html",sorted_array=json_array)

if __name__ == "__main__":
	app.run(debug=True,port=8080)
