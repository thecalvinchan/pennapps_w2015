
playlist_dict = {("positive", "love"):"https://play.spotify.com/user/spotify/playlist/08vPKM3pmoyF6crB2EtASQ" ,
					("positive", "athletic"):"https://play.spotify.com/user/spotify/playlist/7khz2r1UZXAo4G5Z9juehp",
					("positive", "hustle"):"https://play.spotify.com/user/spotify/playlist/7oosV9OVDcTXoyKX1zAGyt",
					("positive", "peaceful"):"https://play.spotify.com/user/spotify/playlist/7jq9hVhkNUyFLN1XivhLvK",
					("negative", "love"):"https://play.spotify.com/user/122724904/playlist/4HxsYV0lUhNWlehhnhFJoV",
					("negative", "athletic"):"https://play.spotify.com/user/spotify/playlist/5p9ILyu1wb4KKHORoXU8nb",
					("negative", "hustle"):"https://play.spotify.com/user/spotify/playlist/3CzHq4FcDqnA5TYN9krrot",
					("negative", "peaceful"):"https://play.spotify.com/user/spotify_netherlands/playlist/3GbdQ33cuuC7fR0xibxir0",}

def find_playlist(mood):
    """Given a tuple of sentiment and category will return a spotify playlist"""
    if mood[0] == "neutral":
        mood = ("positive", mood[1])
    url = playlist_dict.get(mood)

    return url
