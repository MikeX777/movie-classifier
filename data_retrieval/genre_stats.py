import os

genre_dict = dict()
max_size = 0
max_movie_name = ""
num_of_zeros = 0

directory = os.fsencode(".\\data_retrieval\\imdb_genres")

for file in os.listdir(directory):
    f = open(f".\\data_retrieval\\imdb_genres\\{os.fsdecode(file)}", "r")
    genres = f.read().split(",")
    if len(genres) > max_size:
        max_size = len(genres)
        max_movie_name = os.fsdecode(file)
    elif len(genres) == 0:
        num_of_zeros += 1
    f.close()
    for genre in genres:
        if genre not in genre_dict:
            genre_dict[genre] = 1
        else:
            genre_dict[genre] += 1


sorted_genres = sorted(genre_dict.items(), key = lambda kv: kv[1], reverse = True)

f = open(".\\data_retrieval\\imdb_genre_stats.txt", "w")

for genre, count in sorted_genres:
    f.write(f"{genre}: {count}\n")

f.write("\n")
f.write(f"Max Size: {max_size}, Movie: {max_movie_name}\n")
f.write(f"Number of Movies with No Genres: {num_of_zeros}\n")

f.close()