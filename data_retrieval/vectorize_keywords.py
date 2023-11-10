import os
from copy import deepcopy

keyword_dict = dict()
directory = os.fsencode(".\\data\\keywords")
index = 0

for file in os.listdir(directory):
    f = open(f".\\data\\keywords\\{os.fsdecode(file)}", "r")
    keywords = f.read().split(",")
    f.close()
    for keyword in keywords:
        if keyword not in keyword_dict:
            keyword_dict[keyword] = index
            index += 1

num_of_outputs = len(keyword_dict)

f = open(".\\data_retrieval\\keyword_indecies.txt", "w")

for keyword in keyword_dict:
    f.write(f"{keyword}:{keyword_dict[keyword]}\n")

for file in os.listdir(directory):
    f = open(f".\\data\\keywords\\{os.fsdecode(file)}", "r")
    keywords = f.read().split(",")
    f.close()

    out_weights = [0] * num_of_outputs
    for keyword in keywords:
        out_weights[keyword_dict[keyword]] = 1
    
    f = open(f".\\data\\vectorized_keywords_succinct\\{os.fsdecode(file)}", "w")
    f.write("".join(map(lambda x: f"{x},", out_weights))[:-1])
    f.close()



f.close()