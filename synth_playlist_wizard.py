import playlist_handler as plist
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
from gui import *

if os.path.exists("config.bin"):
    with open("config.bin", 'r') as config_file:
        synth_path = config_file.readline()
else:
    synth_path = ""

if synth_path == "":
    Tk().withdraw()
    synth_path = askdirectory()
    with open("config.bin", 'w') as config_file:
        config_file.write(synth_path)

song_path = synth_path + "/CustomSongs/"
playlist_path = synth_path + "/Playlist/"

app = GUI(0)

# load songs info into memory
try:
    song_list = plist.SongLister(song_path)
except FileNotFoundError:
    print("Could not find Synth Riders directory")
    os.remove("config.bin")
    exit(1)

# create playlist sorted by date
song_list.sort_by_date()
newest = plist.PlaylistHandler.new_playlist("newest")
newest.dataString = song_list.to_playlist()
newest.export("newest", playlist_path)

# create playlist sorted by song name z - a
song_list.sort_by_name(True)
ztoa = plist.PlaylistHandler.new_playlist("ztoa")
ztoa.dataString = song_list.to_playlist()
ztoa.export("ztoa", playlist_path)

# create playlist sorted by length
song_list.sort_by_length()
length = plist.PlaylistHandler.new_playlist("length")
length.dataString = song_list.to_playlist()
length.export("length", playlist_path)

# create playlist sorted by bpm
song_list.sort_by_bpm()
bpm = plist.PlaylistHandler.new_playlist("bpm")
bpm.dataString = song_list.to_playlist()
bpm.export("bpm", playlist_path)

app.MainLoop()
