from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import json, main, webbrowser

with open("config.json") as file:
    config = json.loads(file.read())

directory = config["initialdir"]

def saveconfig():
    with open("config.json", "w") as file:
        file.write(",\n".join(json.dumps(config).split(",")))

def browse_event():
    directory = filedialog.askdirectory(initialdir=config["initialdir"], title="Select a folder to download posts to")
    if directory != "":
        config["initialdir"] = directory
    saveconfig()

def download_event():
    main.download_gelbooru(tags_entry.get(), directory, pid_entry.get())
    # print(directory)
    messagebox.showinfo(title="Download", message="Download complete.")

def get_tags_event():
    messagebox.showinfo(title="Tags of " + str(id_entry.get()), message="\n".join(main.get_by_id(int(id_entry.get()))["post"][0]["tags"].split(" ")))
    # print(main.get_by_id(id_entry.get())["post"])

def open_website_event():
    main.open_view(id_entry.get())

def test(arg):
    print(arg)
    print(root.focus_get())
    download_btn.focus_set()

root = Tk()
root.title("gelbooru downloader")
root.resizable(width=False, height=False)

frm = ttk.Frame(root, padding=10)
tags_label = ttk.Label(frm, text="Tags")
tags_entry = ttk.Entry(frm)
download_btn = ttk.Button(frm, text="Download", command=download_event)
browse_btn = ttk.Button(frm, text="Browse...", command=browse_event)
pid_label = ttk.Label(frm, text="Page ID")
pid_entry = ttk.Entry(frm)
id_label = ttk.Label(frm, text="ID")
id_entry = ttk.Entry(frm)
get_tags_btn = ttk.Button(frm, text="Get Tags", command=get_tags_event)
open_website_btn = ttk.Button(frm, text="Open Website", command=open_website_event)


pid_entry.insert(0,"0")
tags_entry.bind("<Enter>", func=test)


tags_label.grid(column=0, row=0)
tags_entry.grid(column=1, row=0)
download_btn.grid(column=2, row=0)
browse_btn.grid(column=3, row=0)
pid_label.grid(column=0, row=1)
pid_entry.grid(column=1, row=1)
id_label.grid(column=0, row=2)
id_entry.grid(column=1, row=2)
get_tags_btn.grid(column=2, row=2)
open_website_btn.grid(column=3, row=2)

frm.pack()
#
# pages_label = ttk.Label(frm, text="Pages", width=60)
# pages_label.pack(fill=Y)

root.mainloop()