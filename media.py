import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_link, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_link
        self.trailer_youtube_url = youtube_trailer

# a function that will play the video in the link provided as a parameter...
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
