import json
import twitter

CONSUMER_KEY = "x9mme4cCpvf0ePlCEQkjLXwUw"
CONSUMER_SECRET = "bA3mkQKsIlIE7HYBLu12TmnC7TNrPZ9OI88HReBN88holz2ivF"
ACCESS_TOKEN_KEY = "1258272840-A2rVBf6XjOADqpQXd7zuSG6O06NAAGqQQpACnBm"
ACCESS_TOKEN_SECRET = "aOkZlTGXUmEZ4fAqJ1UPP4xFp0DXcoPDcsKYIuPcGyjF8"


def get_training_data():
    """Returns training data for the Bayes Classifier from twitter hashtags"""
    api = twitter.Api(consumer_key = CONSUMER_KEY,
                      consumer_secret = CONSUMER_SECRET,
                      access_token_key = ACCESS_TOKEN_KEY,
                      access_token_secret = ACCESS_TOKEN_SECRET)

    data_tuples = []

    emotions = ["romantic", "athletic", "hustle", "peaceful"]

    for emotion in emotions:
        results = api.GetSearch(term="#"+emotion, count=10000, lang="en")
        for result in results:
            data_tuples.append((result.text, emotion))

    return data_tuples

if __name__ == "__main__":
    data = get_training_data()

    with open('training_data.json', 'w') as outfile:
        json.dump(data, outfile)
