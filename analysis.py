from textblob.classifiers import NaiveBayesClassifier
import os
import json
import requests


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "training_data.json")
data = json.load(open(json_url))

print "loaded up data"

HP_API_KEY = "3e7c9928-ae3b-46bf-9410-51458f3b718c"
HP_URL = "https://api.idolondemand.com/1/api/sync/analyzesentiment/v1"
hp_payload = {"language":"eng", "apikey":HP_API_KEY}

bayes = NaiveBayesClassifier(data)

def get_playlist_type(user_tweets):
    """Returns the type of playlist to suggest to the user"""
    category = get_category(user_tweets)
    sentiment = get_sentiment(user_tweets)

    return (sentiment, category)


def get_category(user_tweets):
    """Returns a category based on the training data and user tweets
        using a bayes classifer. """
    results = {}
    for tweet in user_tweets:
        result = bayes.classify(tweet)
        if result not in results:
            results[result] = 1
        else:
            results[result] += 1

        occurence=list(results.values())
        tags=list(results.keys())

    return tags[occurence.index(max(occurence))]


def get_sentiment(user_tweets):
    """Uses HP IdolOnDemand to get the aggregate sentiment
     of the users tweets. It returns either 'positive', or 'negative'"""
    text = u""

    for tweet in user_tweets:
        text = text + ". " + tweet

    hp_payload["text"] = text
    response = requests.get(HP_URL, params=hp_payload)
    resp_dict = json.loads(response.text)

    return resp_dict['aggregate']['sentiment']
