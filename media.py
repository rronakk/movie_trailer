class Movie():

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url,
                 story_line):
        """ Contructor for movie class, which holds all information about movie
        Args:
            movie_title (string):  Title of the movie
            poster_image_url (string) : url for poster image
            trailer_youtube_url (string) : youtube url for trailer
            story_line (string) : movie story line
        """
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.story_line = story_line


