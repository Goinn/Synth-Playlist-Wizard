import json
import time
import os
import zipfile
from datetime import datetime


class PlaylistHandler:

    def __init__(self, name, description, gradient_top, gradient_down, color_title, color_texture, texture, date, data):
        self.name = name
        self.description = description
        self.gradientTop = gradient_top
        self.gradientDown = gradient_down
        self.colorTitle = color_title
        self.colorTexture = color_texture
        self.texture = texture
        self.creationDate = date
        self.dataString = list(data)

    @classmethod
    def from_dict(cls, datadict: dict):
        name = datadict["name"]
        description = datadict["name"]
        gradient_top = datadict["gradientTop"]
        gradient_down = datadict["gradientDown"]
        color_title = datadict["colorTitle"]
        color_texture = datadict["colorTexture"]
        texture = datadict["texture"]
        date = datadict["creationDate"]
        data = datadict["dataString"]
        return cls(name, description, gradient_top, gradient_down, color_title, color_texture, texture, date, data)

    @classmethod
    def from_file(cls, path: str, file: str):
        with open(path + file, "r") as playlist:
            d_play: dict = json.load(playlist)
        name = d_play["name"]
        description = d_play["name"]
        gradient_top = d_play["gradientTop"]
        gradient_down = d_play["gradientDown"]
        color_title = d_play["colorTitle"]
        color_texture = d_play["colorTexture"]
        texture = d_play["texture"]
        date = d_play["creationDate"]
        data = d_play["dataString"]
        return cls(name, description, gradient_top, gradient_down, color_title, color_texture, texture, date, data)

    @staticmethod
    def new_playlist(name):
        return PlaylistHandler(name, "", "#8265FA", "#E83679", "#FFFFFF", "#808080", 0, time.time(), [])

    def add_song(self, song: str):
        self.dataString.append(song.format())

    def to_dict(self):
        p_dict = {
            "namePlaylist": self.name,
            "description": self.description,
            "gradientTop": self.gradientTop,
            "gradientDown": self.gradientDown,
            "colorTitle": self.colorTitle,
            "colorTexture": self.colorTexture,
            "texture": self.texture,
            "creationDate": self.creationDate,
            "dataString": self.dataString
            }
        return p_dict

    def pretty_print(self):
        print(json.dumps(self.to_dict(), indent=4))

    def export(self, file_name, path):
        print("Writing playlist to " + path + file_name + ".playlist")
        with open(path + file_name + ".playlist", 'w') as outfile:
            json.dump(self.to_dict(), outfile, indent=4)


class SongHandler:

    def __init__(self, name, author, difficulties, track_duration, date, bpm, mapper):
        self.name = name
        self.author = author
        self.difficulties = difficulties
        self.difficulty = max(self.filter_difficulty())
        self.trackDuration = self.reformat_duration(track_duration)
        self.date = date
        self.bpm = bpm
        self.mapper = mapper
        # TODO set selected difficulty properly

    @classmethod
    def from_dict(cls, song_dict):
        return cls(song_dict["name"],
                   song_dict["artist"],
                   song_dict["supportedDifficulties"],
                   song_dict["duration"],
                   song_dict["date"],
                   song_dict["bpm"],
                   song_dict["mapper"])

    @classmethod
    def from_dict_old_format(cls, song_dict):
        return cls(song_dict["Name"],
                   song_dict["Author"],
                   SongHandler.get_difficulty_from_track(song_dict["Track"]),
                   0,  # TODO calculate length from first and last orb
                   song_dict["date"],
                   song_dict["BPM"],
                   song_dict["Beatmapper"])

    @staticmethod
    def reformat_duration(duration):
        if not duration:
            minutes = seconds = "0"
        else:
            # strip ":" and prefix '0'
            [minutes, seconds] = str.split(duration, ':')
        return str(int(minutes)) + seconds

    @staticmethod
    def get_difficulty_from_track(track_data):
        difficulty = []
        for dif in track_data:
            if not track_data[dif] == {} and not track_data[dif] is None:
                difficulty += [dif]
            else:
                difficulty += [""]
        return difficulty

    def filter_difficulty(self):
        i = 0
        dif = []
        for difficulty in self.difficulties:
            if not difficulty == "":
                dif.append(i)
            i += 1
        return dif

    def format(self):
        song_dict = {
            "name": self.name,
            "author": self.author,
            "difficulty": self.difficulty,
            "trackDuration": self.trackDuration
        }
        return song_dict


class SongLister:

    def __init__(self, path):
        self.song_list = []
        self.load(path)
    
    def load(self, path):
        # import from song folder path
        for song_file in os.listdir(path):
            if song_file.endswith('.synth'):
                # print(song_file)
                try:
                    with zipfile.ZipFile(path + song_file, 'r') as zip_file:
                        for file in zip_file.filelist:
                            if file.filename == "beatmap.meta.bin":
                                file_date = datetime(*file.date_time[0:6]).strftime("%Y-%m-%d %H:%M:%S")

                        try:
                            with open(zip_file.extract("track.data.json"), "r", encoding='utf16') as song_info:
                                song_dict = json.load(song_info)
                                song_dict["date"] = file_date
                                self.song_list.append(SongHandler.from_dict(song_dict))
                        except KeyError:
                            try:
                                with open(zip_file.extract("beatmap.meta.bin"), "r", encoding='utf-8-sig') as song_info:
                                    song_dict = json.load(song_info)
                                    song_dict["date"] = file_date
                                    self.song_list.append(SongHandler.from_dict_old_format(song_dict))
                            except KeyError:
                                print(" Old synth file format not supported, " + song_file)
                                continue
                except RuntimeError:
                    print(" File is encrypted, " + song_file)

    def sort_by_date(self):
        self.song_list.sort(key=lambda song: song.date, reverse=True)

    def sort_by_name(self, reverse: bool):
        self.song_list.sort(key=lambda song: song.name, reverse=reverse)

    def sort_by_author(self, reverse: bool):
        self.song_list.sort(key=lambda song: song.author, reverse=reverse)

    def sort_by_mapper(self, reverse: bool):
        self.song_list.sort(key=lambda song: song.mapper, reverse=reverse)

    def sort_by_length(self):
        self.song_list.sort(key=lambda song: song.trackDuration)

    def sort_by_bpm(self):
        self.song_list.sort(key=lambda song: song.bpm)

    def to_playlist(self):
        data_string = []
        for song in self.song_list:
            data_string.append(song.format())
        return data_string
