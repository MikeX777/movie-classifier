import os

keyword_dict = dict()

directory = os.fsencode(".\\data_retrieval\\imdb_keywords")

for file in os.listdir(directory):
    f = open(f".\\data_retrieval\\imdb_keywords\\{os.fsdecode(file)}", "r")
    keywords = f.read().split(",")
    f.close()
    for keyword in keywords:
        if keyword not in keyword_dict:
            keyword_dict[keyword] = 1
        else:
            keyword_dict[keyword] += 1


sorted_keywords = sorted(keyword_dict.items(), key = lambda kv: kv[1], reverse = True)

f = open(".\\data_retrieval\\imdb_keyword_stats.txt", "w")

for keyword, count in sorted_keywords:
    f.write(f"{keyword}: {count}\n")

f.close()