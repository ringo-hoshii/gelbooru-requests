import requests
import json
import os, sys, webbrowser

with open("config.json") as file:
    config = json.loads(file.read())

BASE_LINK = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1"
# BLACKLISTED_TAGS = "-milf+-large_breasts"
blacklisted_tags = config["blacklisted_tags"]
gelbooru_view_link = config["gelbooru_view_link"]
chrome_path = config["chrome_path"]

def download_gelbooru(tags="", path="media/", pid=0):
    tags = str(tags)
    if tags != "":
        tags_for_dir = tags
        tags = "+".join(tags.split(" "))
    else:
        tags_for_dir = "undefined"
    tags_for_dir = "_".join(tags_for_dir.split(":"))
    tags = "+".join(blacklisted_tags.split(" ")) + "+" + tags
    r = requests.get(BASE_LINK + "&pid=" + str(pid) + "&tags=" + tags)
    text = json.loads(r.text)
    if not os.path.exists(path + "/" + tags_for_dir):
        os.makedirs(path + "/" + tags_for_dir)
    for i in text["post"]:
        with open(path + "/" + tags_for_dir + "/" + str(i["id"]) + "." + i["file_url"].split("/")[-1].split(".")[-1], "wb") as file:
            imgr = requests.get(i["file_url"])
            file.write(imgr.content)

def get_by_id(id):
    return json.loads(requests.get(BASE_LINK + "&id=" + str(id)).text)

def open_view(id):
    webbrowser.get(chrome_path).open_new_tab(gelbooru_view_link + id)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        tags=""
        pages=1
    else:
        tags=sys.argv[1]
        pages=sys.argv[2]
    download_gelbooru(tags=tags, pid=int(pages))