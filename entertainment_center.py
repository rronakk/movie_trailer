import media
import fresh_tomatoes

# Creating movies list to hold all movies object
movies = [media.Movie("Rounders",
                      "http://cdn.traileraddict.com/vidquad/miramax-films/rounders/1.jpg",
                      "https://www.youtube.com/watch?v=9r-K5dmt0Rc"),
          media.Movie("The Pursuit of Happyness",
                      "https://s-media-cache-ak0.pinimg.com/originals/63/cb/d7/63cbd73759897841f25d626d1480a389.jpg",
                      "https://www.youtube.com/watch?v=89Kq8SDyvfg"),
          media.Movie("Law Abiding Citizen",
                      "http://www.impawards.com/2009/posters/law_abiding_citizen_ver4.jpg",
                      "https://www.youtube.com/watch?v=LX6kVRsdXW4")
          ]


fresh_tomatoes.open_movies_page(movies)
