"""
Orignally Written by Anandh Kumar
Github: https://github.com/anandh-kumar

He has allowed me to use his code.
"""
import random
import string
import scrapetube
import json
from datetime import date

def get_random_link(search_query: str, limit: int = 100):
    print("trying")
    videos = scrapetube.get_search(search_query, limit=limit)
    video_id = []
    for video in videos:
        video_id.append(video["videoId"])
    if len(video_id) == 0:
        get_random_link(search_query)
    return random.choice(video_id)


def get_search_query():
    chars = string.ascii_letters
    search_query = ""
    search_query_len = random.randint(1, 25)

    for _ in range(search_query_len):
        search_query += random.choice(chars)

    return search_query

def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["ids"].update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
 

def main():
    search_query = get_search_query()
    link = get_random_link(search_query)
    linkjson = {str(date.today()):link}
    write_json(linkjson,"ytrandlinks.json")
    print(link)


if __name__ == "__main__":
    main()

