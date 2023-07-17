from PyQt5.QtWidgets import QMessageBox
from pytube import YouTube
import glob
import os
import datetime
import string
import ffmpeg


class VideoDownloader:
    def __init__(self, video_url=None, video_resolution=None, video_audio=None, video_format=None):
        self.video_url = video_url
        self.video_resolution = video_resolution
        self.video_audio = video_audio
        self.format = video_format

    #Creates a list based on the user's input
    def videos_list(self):
        videos_list = self.video_url.split(',')
        return videos_list

    # Get video's details
    def get_video_detail(self, videos_list_func):
        video_title_list = [
            {YouTube(video).title: {"channel": YouTube(video).author, "length": YouTube(video).length,
                                    "date": YouTube(video).publish_date, "views": YouTube(video).views,
                                    "streams": YouTube(video).streams, "thumb": YouTube(video).thumbnail_url}}
            for video in videos_list_func]
        return video_title_list

    # Gets the available resolutions for a given video
    def get_all_resolutions(self, video_streams=None):
        resolution_list = list({stream.resolution for stream in video_streams if stream.resolution is not None})
        all_resolutions = [f"{str(int_resolution)}p" for int_resolution in
                      sorted([int(str_resolution.replace("p", "")) for str_resolution in resolution_list])]
        return all_resolutions

    # Tries to download the selected video (only audio, only video or complete video)
    def download(self, video_title=None, video_streams=None, video_resolution=None, video_format=None, download_detail=None):
        # Removes any special character the video may contain
        string_list = string.ascii_lowercase+string.ascii_uppercase+string.digits+" _-áÁéÉíÍóÓúÚâÂãÃ"
        if download_detail == 'audio_only':
            video_streams.get_audio_only().download(filename=f"{''.join(letter for letter in video_title if letter in string_list)} - {datetime.datetime.now().strftime('%d-%m-%Y')}.mp3", output_path='./Downloads/')
        elif download_detail == 'video_only':
            video = video_streams.filter(progressive=False, resolution=video_resolution, subtype=video_format, only_video=True)
            video.first().download(filename=f"{''.join(letter for letter in video_title if letter in string_list)} - {datetime.datetime.now().strftime('%d-%m-%Y')}.{video_format}", output_path='./Downloads/')
        # Creates a temp folder to store temporary only_audio and only_video files before they get merged
        elif download_detail == 'video_audio':
            try:
                video = video_streams.filter(progressive=False, resolution=video_resolution, subtype=video_format, only_video=True)
                my_video = video.first().download(filename=f"temp_video.{video_format}", output_path='./temp/')
                my_audio = video_streams.get_audio_only().download(filename='temp_audio.mp3', output_path='./temp/')
                ffmpeg.concat(ffmpeg.input(my_video), ffmpeg.input(my_audio), v=1, a=1).output(f"./Downloads/{''.join(letter for letter in video_title if letter in string_list)} - {datetime.datetime.now().strftime('%d-%m-%Y')}.{video_format}").run(overwrite_output=True)
            except ffmpeg.Error as e:
                mensage_dialog = QMessageBox(self)
                mensage_dialog.setStandardButtons(QMessageBox.Ok)
                mensage_dialog.setIcon(QMessageBox.Warning)
                mensage_dialog.setWindowTitle("Error!")
                mensage_dialog.setText(f"{e.stdout.decode('utf8')}\n{e.stderr.decode('utf8')}")
                mensage_dialog.exec()
            finally:
                # Removes the temporary files
                files = glob.glob('./temp/*')
                for file in files:
                    os.remove(file)
