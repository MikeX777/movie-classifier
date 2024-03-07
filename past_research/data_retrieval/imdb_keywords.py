from imdb import Cinemagoer

ia = Cinemagoer()
movie = ia.get_movie('0147800')
ia.update(movie, ["keywords"])
print(movie["keywords"])

# keywords = ia.get_movie_keywords("0147800")

# print(len(keywords['data']['keywords']))