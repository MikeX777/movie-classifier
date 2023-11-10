import os
import time
import re
from imdb import Cinemagoer

# ia = Cinemagoer()

# f = open(".\\imdb_script_stats.txt", "r")

# for line in f.readlines():
#     if os.path.isfile(f".\\imdb_error\\scripts\\{line[:-1]}"):
#             os.rename(f".\\imdb_error\\scripts\\{line[:-1]}", f".\\none_scripts\\{line[:-1]}")

# f.close()

# f = open(".\\imdb_ids.txt", "r")

# for line in f.readlines():

#     try:
#         combined = line[:-1]
#         vals = combined.split(":")

#         # Searching with Movie Name, Resolving Keywords
#         movie = ia.get_movie(vals[1])
#         time.sleep(5)

#         # Get Keywords from Movie IMDB
#         ia.update(movie, ["keywords"])
#         output = "".join(map(lambda x: f"{x},", movie["keywords"]))[:-1]
#         f2 = open(f".\\imdb_error\\keywords\\{vals[0]}", "w")
#         f2.write(output)
#         f2.close()
#         time.sleep(5)

#     except:
#         print(f'Error on {line}')

# f.close()

html_encode_pattern = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
html_comment_pattern = re.compile("<!--([\s\S])*?-->")


directory = os.fsencode(".\\data\\scripts")

for file in os.listdir(directory):
    f = open(f".\\data\scripts\\{os.fsdecode(file)}", "r")
    script = f.read()
    f.close()
    f = open(f".\\data\scripts\\{os.fsdecode(file)}", "w")
    script = re.sub("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", "", script)
    script = re.sub("<!--([\s\S])*?-->", "", script)
    f.write(script)
    f.close()
