import json
from flask_oauth import OAuth
import requests
import base64
import json
import os
from playlist_result import find_playlist
from analysis import *
from flask import (Flask, request, redirect, g, render_template,
                   session, url_for, flash)


app = Flask(__name__, static_url_path="")
app.secret_key = 'Ab!??%/!jmN]LWX/,?RTasoidjfoiajs'
oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='x9mme4cCpvf0ePlCEQkjLXwUw',
    consumer_secret='bA3mkQKsIlIE7HYBLu12TmnC7TNrPZ9OI88HReBN88holz2ivF'
)

@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

@app.route('/')
def index():
    return render_template("index.html",twitter_login=url_for('login'),
        spotify=url_for('spotify_request')
    )

@app.route('/spotify')
def spotify_request():
    print get_twitter_token()
    if get_twitter_token():
        resp = twitter.get('statuses/user_timeline.json',data={'count':10})
        print resp.status
        if resp.status == 200:
            tweets = []
            for tweet in resp.data:
                tweets.append(tweet['text'])
            if len(tweets) > 0:
                print tweets
                result = get_playlist_type(tweets)
                print result
                playlist = find_playlist(result)

                return render_template("spotify.html", playlist=playlist)
            else:
                flash('It looks like you got no tweets!')
                return redirect(url_for('index'))
        else:
            tweets = None
            flash('Unable to load tweets from Twitter. \
                Maybe out of API calls or Twitter is overloaded.')
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/twitterlogin')
def login():
    if get_twitter_token():
        print get_twitter_token()
        return redirect(url_for('oauth_authorized'))
    return twitter.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('step2')
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

@app.route('/step2')
def step2():
    return render_template("step2.html", spotify_redirect = "/spotify")


@app.route('/generate')
def generate():
    """Generates a spotify playlist given a twitter dataset"""
    tweets = ["having a great time at PENNAPPS today",
              "This is so cool, I love this place!"]
    result = get_playlist_type(tweets)
    playlist = find_playlist(result)

    return render_template("result.html", playlist=playlist )


if __name__ == "__main__":
	app.run(debug=True,port=8080)
