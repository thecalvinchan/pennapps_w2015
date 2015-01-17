
def find_playlist((pos_or_neg, emotion)):
	url = "default"
	if pos_or_neg == "positive":
		if emotion == "romantic":
			url = "https://play.spotify.com/user/spotify/playlist/08vPKM3pmoyF6crB2EtASQ"
		elif emotion == "athletic":
			url = "https://play.spotify.com/user/spotify/playlist/5p9ILyu1wb4KKHORoXU8nb"
		elif emotion == "hustle":
			url = "https://play.spotify.com/user/1239967792/playlist/3lxpmR5ptfRFp1DcEqhenT"
		elif emotion == "peaceful":
			url = "https://play.spotify.com/user/spotify/playlist/7jq9hVhkNUyFLN1XivhLvK"
	else:
		if emotion == "romantic":
			url = "https://play.spotify.com/user/spotify_netherlands/playlist/3GbdQ33cuuC7fR0xibxir0"
		elif emotion == "athletic":
			url = "https://play.spotify.com/user/spotify/playlist/3ZSsJYq3of05Rmu3ck5tkO"
		elif emotion == "hustle":
			url = "https://play.spotify.com/user/spotify/playlist/2ujjMpFriZ2nayLmrD1Jgl"
		elif emotion == "peaceful":
			url = "https://play.spotify.com/user/gobins/playlist/2swVZYX6SVh5HbmOXEOg5P"
	
	return url