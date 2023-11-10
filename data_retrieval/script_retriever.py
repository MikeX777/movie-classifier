import requests
import re
import time
import tmdbsimple as tmdb
import imdb
from bs4 import BeautifulSoup
import os.path

ia = imdb.IMDb()
script_base_address = "https://imsdb.com"
script_index_base = "https://imsdb.com/alphabetical/"
scirpt_index_routes = [ "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

movie_paths = dict()

index_pattern = re.compile("href=\"/Movie Scripts/.+?(?=\")")
movie_pattern = re.compile("href=\"/scripts/.+?(?=\")")
clean_pattern = re.compile('<.*?>')

for route in scirpt_index_routes:
    response = requests.get(script_index_base + route)
    index_soup = BeautifulSoup(response.content, 'html.parser')
    matches = index_pattern.findall(str(index_soup))
    cleaned_matches = list(map(lambda x: x.replace("href=\"", ""), matches))

    for cleaned_match in cleaned_matches:
        movieName = cleaned_match[15:-12]
        movieName = movieName.replace(" ", "_").replace(":", "").replace(".", "")
        if movieName not in movie_paths:
            movie_paths[movieName] = cleaned_match
    time.sleep(10)

for movie_name in movie_paths:
    movie_url = script_base_address + movie_paths[movie_name]

    try:
        # Get and save script text
        response = requests.get(movie_url)
        movie_soup = BeautifulSoup(response.content, 'html.parser')
        script_path = movie_pattern.findall(str(movie_soup))[0].replace("href=\"", "")
        script_url = script_base_address + script_path
        script_response = requests.get(script_url)
        script_soup = BeautifulSoup(script_response.content, 'html.parser')
        script_text = re.sub(clean_pattern, "", str(script_soup.find("pre")))
        f = open(f".\\scripts\\{movie_name}.txt", "w")
        f.write(script_text)
        f.close()

        # Searching with Movie Name, Resolving Keywords
        search = ia.search_movie(movie_name.replace("_", " "))
        search_result_id = "tt" + search[0].getID()
        for x in search:
            if str(x).lower() == movie_name.replace("_", " "):
                search_result_id = "tt" + x.getID()
                break

        # Get Keywords from Movie Database
        tmdb.API_KEY = "020ae56768138595de9631a3e689c7ed"
        find = tmdb.Find(search_result_id).info(external_source = "imdb_id")
        keywords = tmdb.Movies(find['movie_results'][0]['id']).keywords()['keywords']
        output = "".join(map(lambda x: f"{x['name']},", keywords))[:-1]
        f = open(f".\\keywords\\{movie_name}.txt", "w")
        f.write(output)
        f.close()
        time.sleep(15)
    except:
        f = open(f".\\error\\errors.txt", "a")
        f.write(f"{movie_name}\n")
        f.close()
        if os.path.isfile(f".\\keywords\\{movie_name}.txt"):
            os.rename(f".\\keywords\\{movie_name}.txt", f".\\error\\keywords\\{movie_name}.txt")

        if os.path.isfile(f".\\scripts\\{movie_name}.txt"):
            os.rename(f".\\scripts\\{movie_name}.txt", f".\\error\\scripts\\{movie_name}.txt")

