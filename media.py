import webbrowser

class Movie():
    """
    Movie class which holds all required information about movies
    """

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


