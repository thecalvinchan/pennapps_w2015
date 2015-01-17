import twitter



# GET /1.1/search/tweets.json?q=%23romantic&lang=en HTTP/1.1
# Authorization:
# OAuth oauth_consumer_key="DC0sePOBbQ8bYdC8r4Smg",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1421518976",oauth_nonce="1733620285",oauth_version="1.0",oauth_token="2982828215-cy4bKei8v2XzhDu4puOiyOkh381x5STMI7wMAv0",oauth_signature="Qh3E22oCzqUOLt6wd1I5GRrA3QU%3D"
# Host:
# api.twitter.com
# X-Target-URI:
# https://api.twitter.com
# Connection:
# Keep-Alive

#Authorization code flow

data_tuples = []

def print_emotions():
	emotions = ["romantic", "athletic", "hustle", "peaceful"]

	for emotion in emotions:
		results = api.GetSearch(term="#"+emotion, count=10000, lang="en")
		for result in results:
			data_tuples.append((result.text, emotion))

	return data_tuples



# Authorization =  "OAuth"
CONSUMER_KEY = "3Sk0imwAY6KS5si5T6msfkteK"
CONSUMER_SECRET = "Nefker0Do9JMShIZwIyCgkzwL4BuZE6xHPj2rsOFJIQKg1Dz1V"
ACCESS_TOKEN_KEY = "2982828215-5Ws0vWxkgkX5diGbELZsda9hu4K9RxTAaa6dPDz"
ACCESS_TOKEN_SECRET = "W4M18csBdvjZSNlIdYraQ6b7Y1ZGlt5meNy6AtN33n6DN"

api = twitter.Api(consumer_key = CONSUMER_KEY,
                      consumer_secret = CONSUMER_SECRET,
                      access_token_key = ACCESS_TOKEN_KEY,
                      access_token_secret = ACCESS_TOKEN_SECRET)






	# url = "https://api.twitter.com/1.1/search/tweets.json?q=%23"+ emotion + "&lang=en"
