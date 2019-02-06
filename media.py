import webbrowser

# define a class movie so that multiple movies can be created as objects under this class with storyline, 
# poster, and trailer.

class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    # add a show_trailer method to the movie class.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# define a Video class that will contain title and duration.

class Video():
    def __init__(self, title, duration):
        self.title = video.title
        self.duration = video.duration
