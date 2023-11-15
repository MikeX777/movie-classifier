import os

files = []
max_lines = 0
movie_name = ""

directory = os.fsencode(".\\data\\scripts")

for file in os.listdir(directory):
    f = open(f".\\data\\scripts\\{os.fsdecode(file)}", "r", encoding='utf-8')
    text = f.read().split("\n")
    if len(text) > max_lines:
        max_lines = len(text)
        movie_name = os.fsdecode(file)
    if len(text) > 6000:
        files.append({"name": os.fsdecode(file), "lines": len(text)})

print(f"Max Lines: {max_lines}\n")
print(f"Movie Name: {movie_name}\n")
print(files)