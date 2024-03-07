import os
from copy import deepcopy
import csv
import numpy

genre_dict = dict()
directory = os.fsencode(".\\data_retrieval\\imdb_genres")
index = 0
max_num_of_genres = 0
csv

for file in os.listdir(directory):
    f = open(f".\\data_retrieval\\imdb_genres\\{os.fsdecode(file)}", "r")
    genres = f.read().split(",")
    f.close()
    if len(genres) > max_num_of_genres:
        max_num_of_genres = len(genres)
    for genre in genres:
        if genre not in genre_dict:
            genre_dict[genre] = index
            index += 1

num_of_outputs = len(genre_dict)

f = open(".\\data_retrieval\\genre_indecies.txt", "w")

for genre in genre_dict:
    f.write(f"{genre}:{genre_dict[genre]}\n")
f.close()

for file in os.listdir(directory):
    f = open(f".\\data\\genres\\{os.fsdecode(file)}", "r")
    genres = f.read().split(",")
    f.close()

    out_weights = [0] * num_of_outputs
    for genre in genres:
        out_weights[genre_dict[genre]] = 1

    f = open(f".\\data\\vectorized_genres_succinct\\{os.fsdecode(file)}", "w")
    f.write("".join(map(lambda x: f"{x},", out_weights))[:-1])
    f.close()


    # out_weights = numpy.zeros((max_num_of_genres, num_of_outputs))
    # for idx, genre in enumerate(genres):
    #     out_weights[idx][genre_dict[genre]] = 1
    
    # with open(f".\\data\\vectorized_genres_succinct\\{os.fsdecode(file)}", "w", newline='') as csvfile:
    #     wr = csv.writer(csvfile)
    #     wr.writerows(out_weights)



f.close()