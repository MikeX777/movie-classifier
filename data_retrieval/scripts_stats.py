import os

error_scripts = []
directory = os.fsencode(".\\imdb_error\\scripts")

for file in os.listdir(directory):
    f = open(f".\\imdb_error\\scripts\\{os.fsdecode(file)}", "r")
    all_lines = f.readlines()
    f.close()
    if len(all_lines) < 20:
        error_scripts.append(file)

f = open(".\\imdb_script_stats.txt", "w")

for error in error_scripts:
    f.write(f"{os.fsdecode(error)}\n")

f.close()