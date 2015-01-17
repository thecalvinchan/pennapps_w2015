import json
from flask import Flask, request, redirect, g, render_template
import requests
import base64
from textblob.classifiers import NaiveBayesClassifier
import json
from training import print_emotions

app = Flask(__name__, static_url_path="")

#Authorization code flow
url = "https://accounts.spotify.com/authorize"
CLIENT_ID = "29262729c4fa49afaf21f40f56feb5cf"
REDIRECT_URI = "http://127.0.0.1:8080/callback/q"
SCOPE = "user-modify-private user-modify-public"
CLIENT_SECRET = "25fcda1a3c154584905e996935cc68b8"

HP_API_KEY = "3e7c9928-ae3b-46bf-9410-51458f3b718c"
HP_URL = "https://api.idolondemand.com/1/api/sync/analyzesentiment/v1"
hp_payload = {"language":"eng", "apikey":HP_API_KEY}



payload = {"client_id":CLIENT_ID,
           "response_type":"code",
           "redirect_uri":REDIRECT_URI,
           "scope":SCOPE}

@app.route('/')
def index():
    s_redirect = "https://accounts.spotify.com/authorize/?client_id=" +  \
    CLIENT_ID+ "&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3 \
    A8080%2Fcallback%2Fq&scope=playlist-modify-public+playlist-modify-private"
    return render_template("index.html", spotify_redirect=s_redirect)

@app.route('/generate')
def generate():
    """Generates a spotify playlist given a twitter dataset"""
    return render_template("index.html", )


@app.route("/callback/q")
def callback():
	access_token = request.args
	code_payload = {"grant_type":"authorization_code","code":str(access_token['code']),"redirect_uri":REDIRECT_URI}
	base64encoded = base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET)
	headers = {"Authorization":"Basic %s" % base64encoded}
	post_request = requests.post("https://accounts.spotify.com/api/token",data=code_payload,headers=headers)
	json_response = json.loads(post_request.text)
	test_response = requests.get("https://api.spotify.com/v1/me", headers={'Authorization':'Bearer ' + json_response[u'access_token']})
	json_profile = json.loads(test_response.text)
	playlists = requests.get(json_profile['href']+"/playlists", headers={'Authorization':'Bearer '+json_response[u'access_token']})
	jsoned_playlists = json.loads(playlists.text)
	json_array = []
	for playlist in jsoned_playlists['items']:
		json_array.append(playlist)
	return render_template("index.html",sorted_array=json_array)

def get_category(training_data, users_tweets):
    """Returns a category based on the training data and user tweets
        using a bayes classifer. """
    bayes = NaiveBayesClassifier(training_data)
    results = {}
    for tweet in user_tweets:
        result = bayes.classify(tweet)
        if result not in results:
            results[result] = 1
        else:
            results[result] += 1

        occurence=list(results.values())
        tags=list(results.keys())

    return tags[v.index(max(occurence))]


def get_tweets_sentiment(users_tweets):
    """Uses HP IdolOnDemand to get the aggregate sentiment
     of the users tweets. It returns either 'positive', or 'negative'"""
    text = ""

    for tweet in user_tweets:
        text = text + ". " + tweet

    hp_payload["text"] = text
    response = requests.get(HP_URL, params=hp_payload)
    resp_dict = json.loads(response.text)

    return resp_dict['aggregate']['sentiment']


if __name__ == "__main__":
	app.run(debug=True,port=8080)
