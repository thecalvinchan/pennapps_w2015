
playlist_dict = {("positive", "romantic"):"https://play.spotify.com/user/spotify/playlist/08vPKM3pmoyF6crB2EtASQ",
					("positive", "athletic"):"https://play.spotify.com/user/spotify/playlist/5p9ILyu1wb4KKHORoXU8nb",
					("positive", "hustle"):"https://play.spotify.com/user/1239967792/playlist/3lxpmR5ptfRFp1DcEqhenT",
					("positive", "peaceful"):"https://play.spotify.com/user/spotify/playlist/7jq9hVhkNUyFLN1XivhLvK",
					("negative", "romantic"):"https://play.spotify.com/user/spotify_netherlands/playlist/3GbdQ33cuuC7fR0xibxir0",
					("negative", "athletic"):"https://play.spotify.com/user/spotify/playlist/3ZSsJYq3of05Rmu3ck5tkO",
					("negative", "hustle"):"https://play.spotify.com/user/spotify/playlist/2ujjMpFriZ2nayLmrD1Jgl",
					("negative", "peaceful"):"https://play.spotify.com/user/gobins/playlist/2swVZYX6SVh5HbmOXEOg5P",}

def find_playlist(mood):
	url = playlist_dict.get(mood)
	return url
