import imdb
import time

ia = imdb.Cinemagoer()

actionTop50 = ia.search_movie("Adventure")

print(actionTop50)
print(len(actionTop50))