# gelbooru-requests
Script that is downloading recent gelbooru media specified by tags.

# Prerequisites
You should have Python installed with "requests" library that can be downloaded through "pip install requests".

# Installation
Before proceeding to practical use, you need to clone the repository.
It can be done in two ways:
1. Download ZIP-archive
2. In the command line type "git clone http://github.com/ringo-hoshii/gelbooru-requests"

# Usage
## GUI
Graphical interface is quite intuitive, you just use it as the site.

### Quick Start
For basic usage, just type the tags in, click Browse, select the folder for media to be downloaded to, click Download.
While downloading, process will not respond. It's intended behaviour, so you just need to wait.

### Additional features
You can get a message box with the list of tags of a specific post. To do so, type ID in the corresponding field and click Get Tags. You can also open it in browser instead.

## CLI
python main.py "tags" pid

Tags is the same text as the one you put in search field on the site, including metadata.
This will download 100 posts on specified page (0 by default) in ./media/[TAGS]/ (inside the folder named as the tags you typed in inside the folder "media" inside current folder).

Example:
python \~/gelbooru-requests/main.py "1girl purple_hair animated rating:general" 0

Say, your current working directory is \~/Downloads/Pictures/Anime/
The script will download posts in "\~/Downloads/Pictures/Anime/media/1girl purple_hair animated rating_general"
