from imdb import Cinemagoer
import os
import time

imdb_ids = dict()
genre_values = dict()

ia = Cinemagoer()

f = open("./data_retrieval/imdb_genres_errors.txt", "r", encoding="utf-8")
errors = f.read().split("\n")
f.close()

for error in errors:
    data = error.split(":")
    try:
        movie = ia.get_movie(data[1])
        time.sleep(5)
        output = "".join(map(lambda x: f"{x},", movie["genres"]))
        if len(output) > 0:
            output = output[:-1]
        f = open(f"./data_retrieval/imdb_genres/{data[0]}", "w", encoding = "utf-8")
        f.write(output)
        f.close()

        f = open(f"./data_retrieval/imdb_ids.txt", "a", encoding="utf-8")
        f.write(f"{data[0]}:{data[1]}\n")
        f.close()
    except Exception as ex:
        print(data[0])
        print(ex)
        f = open(f".\\data_retrieval\\imdb_genres_errors_2.txt", "a")
        f.write(f"{data[0]}:{data[1]}\n")
        f.close()


# f = open("./data_retrieval/imdb_ids.txt", "r")
# current = f.read()
# f.close()
# ia = Cinemagoer()

# for line in current.split("\n"):
#     if line.strip():
#         data = line.split(":")
#         if data[0] not in imdb_ids:
#             imdb_ids[data[0]] = data[1]


# directory = os.fsencode("./data_retrieval/imdb_scripts")

# for file in os.listdir(directory):
#     movie_name = os.fsdecode(file)
#     output = ""
#     try:
#         if movie_name not in imdb_ids:
#             # Searching with Movie Name, Resolving genres
#             search = ia.search_movie(movie_name.replace("_", " "))
#             time.sleep(5)
#             search_moive = search[0]
#             for x in search:
#                 if str(x).lower() == movie_name.replace("_", " "):
#                     search_moive = x
#                     break
#             imdb_ids[movie_name] = search_moive.getID()
#             ia.update(search_moive)
#             time.sleep(5)
#             output = "".join(map(lambda x: f"{x},", search_moive["genres"]))
#             if len(output) > 0:
#                 output = output[:-1]
#         else:
#             movie = ia.get_movie(imdb_ids[movie_name])
#             time.sleep(5)
#             output = "".join(map(lambda x: f"{x},", movie["genres"]))
#             if len(output) > 0:
#                 output = output[:-1]
#         f = open(f"./data_retrieval/imdb_genres/{movie_name}", "w", encoding = "utf-8")
#         f.write(output)
#         f.close()
#     except Exception as ex:
#         print(movie_name)
#         print(ex)
#         f = open(f".\\data_retrieval\\imdb_genres_errors.txt", "a")
#         f.write(f"{movie_name}\n")
#         f.close()

#     f = open(f"./data_retrieval/imdb_ids.txt", "w", encoding = "utf-8")
#     for movie in imdb_ids:
#         f.write(movie + ":" + imdb_ids[movie] + "\n")
#     f.close()

