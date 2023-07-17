# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/yVideoDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1465, 504)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(1060, 20, 391, 401))
        self.groupBox.setObjectName("groupBox")
        self.labelThumb = QtWidgets.QLabel(self.groupBox)
        self.labelThumb.setGeometry(QtCore.QRect(10, 20, 371, 181))
        self.labelThumb.setText("")
        self.labelThumb.setPixmap(QtGui.QPixmap("UI\\../Botao_download_canal.png"))
        self.labelThumb.setScaledContents(True)
        self.labelThumb.setObjectName("labelThumb")
        self.labelName = QtWidgets.QLabel(self.groupBox)
        self.labelName.setGeometry(QtCore.QRect(14, 210, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setText("")
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setWordWrap(True)
        self.labelName.setObjectName("labelName")
        self.labelChannel = QtWidgets.QLabel(self.groupBox)
        self.labelChannel.setGeometry(QtCore.QRect(10, 260, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.labelChannel.setFont(font)
        self.labelChannel.setObjectName("labelChannel")
        self.labelDate = QtWidgets.QLabel(self.groupBox)
        self.labelDate.setGeometry(QtCore.QRect(10, 290, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.labelViews = QtWidgets.QLabel(self.groupBox)
        self.labelViews.setGeometry(QtCore.QRect(10, 320, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.labelViews.setFont(font)
        self.labelViews.setObjectName("labelViews")
        self.labelLength = QtWidgets.QLabel(self.groupBox)
        self.labelLength.setGeometry(QtCore.QRect(10, 350, 291, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.labelLength.setFont(font)
        self.labelLength.setObjectName("labelLength")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(580, 150, 441, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.frameRadioButtons = QtWidgets.QFrame(self.groupBox_2)
        self.frameRadioButtons.setEnabled(False)
        self.frameRadioButtons.setGeometry(QtCore.QRect(20, 20, 411, 51))
        self.frameRadioButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRadioButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRadioButtons.setObjectName("frameRadioButtons")
        self.radioButton = QtWidgets.QRadioButton(self.frameRadioButtons)
        self.radioButton.setGeometry(QtCore.QRect(0, 10, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frameRadioButtons)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 10, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frameRadioButtons)
        self.radioButton_3.setGeometry(QtCore.QRect(310, 10, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.comboBoxResolution = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxResolution.setEnabled(False)
        self.comboBoxResolution.setGeometry(QtCore.QRect(120, 84, 302, 31))
        self.comboBoxResolution.setObjectName("comboBoxResolution")
        self.comboBoxResolution.addItem("")
        self.comboBoxResolution.setItemText(0, "")
        self.comboBoxResolution.addItem("")
        self.comboBoxResolution.setItemText(1, "")
        self.labelResolution = QtWidgets.QLabel(self.groupBox_2)
        self.labelResolution.setEnabled(False)
        self.labelResolution.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelResolution.setFont(font)
        self.labelResolution.setObjectName("labelResolution")
        self.downloadButton = QtWidgets.QPushButton(self.groupBox_2)
        self.downloadButton.setEnabled(False)
        self.downloadButton.setGeometry(QtCore.QRect(340, 230, 93, 28))
        self.downloadButton.setObjectName("downloadButton")
        self.clearButton = QtWidgets.QPushButton(self.groupBox_2)
        self.clearButton.setEnabled(False)
        self.clearButton.setGeometry(QtCore.QRect(240, 230, 93, 28))
        self.clearButton.setObjectName("clearButton")
        self.comboBoxFormat = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxFormat.setEnabled(False)
        self.comboBoxFormat.setGeometry(QtCore.QRect(120, 144, 302, 31))
        self.comboBoxFormat.setObjectName("comboBoxFormat")
        self.labelFormat = QtWidgets.QLabel(self.groupBox_2)
        self.labelFormat.setEnabled(False)
        self.labelFormat.setGeometry(QtCore.QRect(20, 150, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelFormat.setFont(font)
        self.labelFormat.setObjectName("labelFormat")
        self.confirmVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmVideoButton.setGeometry(QtCore.QRect(10, 100, 161, 31))
        self.confirmVideoButton.setObjectName("confirmVideoButton")
        self.urlLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLineEdit.setGeometry(QtCore.QRect(10, 60, 931, 31))
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.videosList = QtWidgets.QListWidget(self.centralwidget)
        self.videosList.setGeometry(QtCore.QRect(10, 150, 541, 271))
        self.videosList.setObjectName("videosList")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 631, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelDownloadstatus = QtWidgets.QLabel(self.centralwidget)
        self.labelDownloadstatus.setGeometry(QtCore.QRect(10, 462, 1441, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.labelDownloadstatus.setFont(font)
        self.labelDownloadstatus.setText("")
        self.labelDownloadstatus.setObjectName("labelDownloadstatus")
        self.labelTimer = QtWidgets.QLabel(self.centralwidget)
        self.labelTimer.setGeometry(QtCore.QRect(10, 480, 1441, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.labelTimer.setFont(font)
        self.labelTimer.setText("")
        self.labelTimer.setObjectName("labelTimer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1465, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.comboBoxResolution.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Y Video Downloader"))
        self.groupBox.setTitle(_translate("MainWindow", "Video details"))
        self.labelChannel.setText(_translate("MainWindow", "Channel: "))
        self.labelDate.setText(_translate("MainWindow", "Publication date:"))
        self.labelViews.setText(_translate("MainWindow", "Views: "))
        self.labelLength.setText(_translate("MainWindow", "Length:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Download details"))
        self.radioButton.setText(_translate("MainWindow", "Video and audio"))
        self.radioButton_2.setText(_translate("MainWindow", "Audio only"))
        self.radioButton_3.setText(_translate("MainWindow", "Video only"))
        self.labelResolution.setText(_translate("MainWindow", "Resolution:"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.labelFormat.setText(_translate("MainWindow", "Format:"))
        self.confirmVideoButton.setText(_translate("MainWindow", "Confirm video"))
        self.urlLineEdit.setPlaceholderText(_translate("MainWindow", "Paste the video URL here. To download multiple videos, use a comma (,) as separator."))
        self.label_2.setText(_translate("MainWindow", "Y Video Downloader"))