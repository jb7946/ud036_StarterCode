import media
import fresh_tomatoes

# toy story data
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

#avatar data
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

# the dark knight data
the_dark_knight = media.Movie("The Dark Knight",
                              "A vigilante rises to save Gotham",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# school of rock data
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

#ratatouille data
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=1yKqLNnxGZw")

#mightnight in paris data
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
#hunger games data
hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

#build movies dynamic data and write to fresh_tomatoes.html
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, the_dark_knight]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
