from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from scripts import yVideoDownloader
from scripts.VideoDownloader import VideoDownloader
import math
import urllib.request
import PyQt5.QtGui
import datetime
import threading
import time


class MainWindow(QtWidgets.QMainWindow, yVideoDownloader.Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # Creating a variable to receive video's information and to store the elapsed time in downloads
        self.videos_dict = None
        self.elapsed_time = None

        # Creating the events based on user's action
        self.confirmVideoButton.clicked.connect(lambda: self.confirm_button_clicked())
        self.videosList.itemClicked.connect(lambda: self.select_video())
        self.comboBoxResolution.currentIndexChanged.connect(lambda: self.select_video_format())
        self.comboBoxFormat.currentIndexChanged.connect(lambda: self.activate_buttons())
        self.radioButton.clicked.connect(lambda: self.video_radio_button_checked())
        self.radioButton_2.clicked.connect(lambda: self.audio_radio_button_checked())
        self.radioButton_3.clicked.connect(lambda: self.video_radio_button_checked())
        self.clearButton.clicked.connect(lambda: self.clear_button_clicked())
        self.downloadButton.clicked.connect(lambda: self.download_button_clicked())

    # Creates a new thread to call confirm_video_url function, and clears the lineEdit and videosList
    def confirm_button_clicked(self):
        self.confirmVideoButton.setEnabled(False)
        self.videosList.clear()
        self.labelDownloadstatus.setText("Loading videos, please wait. This action may take few minutes")
        confirming_video = threading.Thread(target=self.confirm_video_url)
        confirming_video.start()
        self.urlLineEdit.clear()

    # Tries to load the given videos in videosList. In case of failure, shows an error message in labelDownloadstatus
    def confirm_video_url(self):
        try:
            confirmation_helper = VideoDownloader(video_url=self.urlLineEdit.text())
            self.videos_dict = confirmation_helper.get_video_detail(confirmation_helper.videos_list())
            for video in confirmation_helper.get_video_detail(confirmation_helper.videos_list()):
                self.videosList.addItem(list(video)[0])
            self.confirmVideoButton.setEnabled(True)
            self.labelDownloadstatus.setText("")
        except Exception as e:
            self.labelDownloadstatus.setText("Error in video confirmation! Did you paste a valid link and / or paste different links using comma?")
            self.confirmVideoButton.setEnabled(True)

    # Gets the selected video details
    def select_video(self):
        try:
            selected_video = self.videosList.currentItem().text()
            self.comboBoxResolution.clear()
            # If user selects a video, radio buttons will be enabled and comboboxResolution will be filled with available resolutions
            if selected_video:
                self.frameRadioButtons.setEnabled(True)
                resolution_list = VideoDownloader().get_all_resolutions(self.videos_dict[self.videosList.currentIndex().row()][selected_video]['streams'])
                for resolution in resolution_list:
                    self.comboBoxResolution.addItem(resolution)
                # Shows the video details
                self.labelName.setText(selected_video)
                self.labelChannel.setText(f"Channel : {self.videos_dict[self.videosList.currentIndex().row()][selected_video]['channel']}")
                self.labelDate.setText(f"Publication date : {datetime.datetime.strftime(self.videos_dict[self.videosList.currentIndex().row()][selected_video]['date'], '%d/%m/%Y')}")
                self.labelViews.setText(f"Views : {self.videos_dict[self.videosList.currentIndex().row()][selected_video]['views']}")
                minutes = math.floor(self.videos_dict[self.videosList.currentIndex().row()][selected_video]['length'] / 60)
                seconds = self.videos_dict[self.videosList.currentIndex().row()][selected_video]['length'] % 60
                self.labelLength.setText(f"Length : {minutes}:{seconds} minutes")
                image = urllib.request.urlopen(self.videos_dict[self.videosList.currentIndex().row()][selected_video]['thumb']).read()
                my_pixmap = PyQt5.QtGui.QPixmap()
                my_pixmap.loadFromData(image)
                self.labelThumb.setPixmap(my_pixmap)
        except Exception as e:
            mensage_dialog = QMessageBox(self)
            mensage_dialog.setStandardButtons(QMessageBox.Ok)
            mensage_dialog.setIcon(QMessageBox.Warning)
            mensage_dialog.setWindowTitle("Error!")
            mensage_dialog.setText(f"{e}")
            mensage_dialog.exec()

    # Gets the available formats
    def select_video_format(self):
        try:
            self.comboBoxFormat.clear()
            resolution = self.comboBoxResolution.currentText()
            formats_set = set()
            for stream in self.videos_dict[self.videosList.currentIndex().row()][self.videosList.currentItem().text()]["streams"].filter(resolution=resolution, progressive=False):
                formats_set.add(stream.subtype)
            for video_format in list(formats_set):
                if video_format != '3gpp':
                    self.comboBoxFormat.addItem(video_format)
        except Exception as e:
            mensage_dialog = QMessageBox(self)
            mensage_dialog.setStandardButtons(QMessageBox.Ok)
            mensage_dialog.setIcon(QMessageBox.Warning)
            mensage_dialog.setWindowTitle("Error!")
            mensage_dialog.setText(f"{e}")
            mensage_dialog.exec()
        finally:
            self.activate_buttons()

    # If user selects a radio button, dowload options will be enabled
    def video_radio_button_checked(self):
        self.comboBoxResolution.setEnabled(True)
        self.labelResolution.setEnabled(True)
        self.labelFormat.setEnabled(True)
        self.comboBoxFormat.setEnabled(True)
        self.activate_buttons()

    def audio_radio_button_checked(self):
        self.comboBoxResolution.setEnabled(False)
        self.labelResolution.setEnabled(False)
        self.comboBoxFormat.setEnabled(False)
        self.labelFormat.setEnabled(False)
        self.activate_buttons()

    def activate_buttons(self):
        if (self.comboBoxFormat.currentIndex() != -1) and (self.comboBoxResolution.currentIndex() != -1) and (self.radioButton.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked()):
            self.clearButton.setEnabled(True)
            self.downloadButton.setEnabled(True)

    # Clears the layout
    def clear_button_clicked(self):
        self.urlLineEdit.clear()
        self.comboBoxResolution.clear()
        self.comboBoxFormat.clear()
        self.comboBoxResolution.setEnabled(False)
        self.comboBoxFormat.setEnabled(False)
        self.labelFormat.setEnabled(False)
        self.labelResolution.setEnabled(False)
        self.radioButton.setChecked(False)
        self.frameRadioButtons.setEnabled(False)
        self.videosList.clear()
        self.labelThumb.clear()
        self.labelName.setText("")
        self.labelChannel.setText("Channel: ")
        self.labelViews.setText("Views: ")
        self.labelLength.setText("Length: ")
        self.labelDate.setText("Publication date: ")
        self.downloadButton.setEnabled(False)
        self.clearButton.setEnabled(False)

    # Creates a new thread to download the video, and other thread to set the elapsed time
    def download_button_clicked(self):
        try:
            self.comboBoxResolution.setEnabled(False)
            self.comboBoxFormat.setEnabled(False)
            self.labelFormat.setEnabled(False)
            self.labelResolution.setEnabled(False)
            self.radioButton.setChecked(False)
            self.frameRadioButtons.setEnabled(False)
            self.downloadButton.setEnabled(False)
            self.clearButton.setEnabled(False)
            downloading = threading.Thread(target=self.download_video, args=["Download finished!"])
            downloading.start()
            if downloading.is_alive():
                self.labelDownloadstatus.setText(f"Downloading video {self.videosList.currentItem().text()}. Please wait...")
                self.videosList.setEnabled(False)
                elapsed_time = threading.Thread(target=self.timer)
                elapsed_time.start()
        except Exception as e:
            mensage_dialog = QMessageBox(self)
            mensage_dialog.setStandardButtons(QMessageBox.Ok)
            mensage_dialog.setIcon(QMessageBox.Warning)
            mensage_dialog.setWindowTitle("Error!")
            mensage_dialog.setText(f"Download Error!\n{e}\nPlease try again!")
            mensage_dialog.exec()

    # Downloads the selected video and restarts the layout
    def download_video(self, message):
        download_detail = ''
        if self.radioButton.isChecked():
            download_detail = 'video_audio'
        elif self.radioButton_2.isChecked():
            download_detail = 'audio_only'
        elif self.radioButton_3.isChecked():
            download_detail = 'video_only'
        VideoDownloader().download(video_title=self.videosList.currentItem().text(), video_streams=
            self.videos_dict[self.videosList.currentIndex().row()][self.videosList.currentItem().text()]['streams'],
                                       download_detail=download_detail,
                                       video_resolution=self.comboBoxResolution.currentText(),
                                       video_format=self.comboBoxFormat.currentText())

        self.labelDownloadstatus.setText(message)
        self.elapsed_time = 1
        self.videos_dict.pop(self.videosList.currentIndex().row())
        self.videosList.takeItem(self.videosList.row(self.videosList.currentItem()))
        self.videosList.clearSelection()
        self.frameRadioButtons.setEnabled(False)
        self.labelThumb.clear()
        self.labelName.setText("")
        self.labelChannel.setText("Channel: ")
        self.labelViews.setText("Views: ")
        self.labelLength.setText("Length: ")
        self.labelDate.setText("Publication date: ")
        self.downloadButton.setEnabled(False)
        self.clearButton.setEnabled(False)
        self.comboBoxResolution.clear()
        self.comboBoxFormat.clear()
        self.videosList.setEnabled(True)

    # Elapsed time configuration
    def timer(self):
        self.elapsed_time = 0
        timer = 0
        while self.elapsed_time == 0:
            time.sleep(1)
            timer += 1
            self.labelTimer.setText(f"Elapsed time: {timer} seconds")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
