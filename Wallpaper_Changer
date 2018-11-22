#!/usr/bin/env python3
import requests
import sys
import os

ACCESS_KEY = ""
API_END_POINT = "https://api.unsplash.com/photos/random"
query = ""

def __main__():
    query = sys.argv[1]
    print("Getting a random wallpaper...")
    get_data = requests.get(API_END_POINT, params={"client_id":ACCESS_KEY, "w":1920, "h":1080, "orientation":"landscape", "query":query})
    json_data = get_data.json()
    print("Download in progress...")
    file = requests.get(json_data["urls"]["full"])
    open("/home/athul/bin/.walli.jpg","wb+").write(file.content)
    os.system("gsettings set org.gnome.desktop.background picture-uri " + "file:///home/athul/bin/.walli.jpg")
    print("Succesfully changed the wallpaper.")


if __name__ == __main__():
    pass

