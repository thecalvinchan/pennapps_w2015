
playlist_dict = {("positive", "romantic"):"08vPKM3pmoyF6crB2EtASQ",
					("positive", "athletic"):"5p9ILyu1wb4KKHORoXU8nb",
					("positive", "hustle"):"3lxpmR5ptfRFp1DcEqhenT",
					("positive", "peaceful"):"7jq9hVhkNUyFLN1XivhLvK",
					("negative", "romantic"):"3GbdQ33cuuC7fR0xibxir0",
					("negative", "athletic"):"3ZSsJYq3of05Rmu3ck5tkO",
					("negative", "hustle"):"2ujjMpFriZ2nayLmrD1Jgl",
					("negative", "peaceful"):"2swVZYX6SVh5HbmOXEOg5P",}

def find_playlist(mood):
	url = "https://play.spotify.com/user/spotify/playlist/" + \
    playlist_dict.get(mood)
	return url
