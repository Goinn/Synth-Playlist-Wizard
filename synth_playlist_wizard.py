import playlist_handler as plist
import json

synth_path = "H:\\Program Files (x86)\\Steam\\steamapps\\common\\SynthRiders\\"
song_path = synth_path + "CustomSongs\\"
playlist_path = synth_path + "Playlist\\"
file = "karaoke riders.playlist"

# load songs info into memory
song_list = plist.SongLister(song_path)

# create playlist sorted by date
song_list.sort_by_date()
newest = plist.PlaylistHandler.new_playlist("newest")
newest.dataString = song_list.to_playlist()
newest.export("newest")

# create playlist sorted by song name z - a
song_list.sort_by_name(True)
ztoa = plist.PlaylistHandler.new_playlist("ztoa")
ztoa.dataString = song_list.to_playlist()
ztoa.export("ztoa")

# create playlist sorted by length
song_list.sort_by_length()
length = plist.PlaylistHandler.new_playlist("length")
length.dataString = song_list.to_playlist()
length.export("length")

# create playlist sorted by bpm
song_list.sort_by_bpm()
bpm = plist.PlaylistHandler.new_playlist("bpm")
bpm.dataString = song_list.to_playlist()
bpm.export("bpm")
