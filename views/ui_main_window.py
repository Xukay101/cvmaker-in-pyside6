# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import assets.images.logocv_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QSize(900, 700))
        MainWindow.setMaximumSize(QSize(900, 700))
        MainWindow.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget = QFrame(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setFrameShape(QFrame.StyledPanel)
        self.centralWidget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.centralWidget)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setAutoFillBackground(False)
        self.background_frame.setStyleSheet(u"background-color: #F4F4F4;")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.stacked_widget = QStackedWidget(self.background_frame)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setEnabled(True)
        self.stacked_widget.setGeometry(QRect(230, 0, 671, 701))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.frame_10 = QFrame(self.page_1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 640, 671, 61))
        self.frame_10.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.button_16 = QPushButton(self.frame_10)
        self.button_16.setObjectName(u"button_16")
        self.button_16.setGeometry(QRect(490, 10, 161, 31))
        self.button_16.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame_24 = QFrame(self.page_1)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(0, 0, 671, 641))
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.frame_24)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(60, 300, 541, 161))
        self.label_26.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_26.setTextFormat(Qt.MarkdownText)
        self.label_26.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_26.setWordWrap(True)
        self.label_32 = QLabel(self.frame_24)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(270, 270, 141, 31))
        self.label_32.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 25px;")
        self.label_32.setTextFormat(Qt.MarkdownText)
        self.label_32.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_32.setWordWrap(True)
        self.label_33 = QLabel(self.frame_24)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(210, 20, 251, 241))
        self.label_33.setStyleSheet(u"border-image: url(:/cct/logo-cv.png);")
        self.stacked_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 640, 671, 61))
        self.frame_11.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.button_18 = QPushButton(self.frame_11)
        self.button_18.setObjectName(u"button_18")
        self.button_18.setGeometry(QRect(490, 10, 161, 31))
        self.button_18.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_19 = QPushButton(self.frame_11)
        self.button_19.setObjectName(u"button_19")
        self.button_19.setGeometry(QRect(20, 10, 161, 31))
        self.button_19.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame_19 = QFrame(self.page_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(100, 50, 481, 251))
        self.frame_19.setStyleSheet(u"border:0px;\n"
"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(140, 40, 211, 181))
        self.frame_20.setStyleSheet(u"background-color: #4a8dac;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_35 = QLabel(self.frame_20)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(0, 0, 211, 181))
        self.label_35.setStyleSheet(u"border-image: url(:/cct/avatar_default_12_545452.png);")
        self.label_36 = QLabel(self.frame_20)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setEnabled(True)
        self.label_36.setGeometry(QRect(-3, -3, 221, 191))
        self.frame_28 = QFrame(self.frame_19)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(129, 29, 231, 201))
        self.frame_28.setStyleSheet(u"background-color: #f7b733;\n"
"border-radius: 10px;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_28.raise_()
        self.frame_20.raise_()
        self.frame_21 = QFrame(self.page_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(100, 300, 481, 231))
        self.frame_21.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 25px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 20px;\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.button_15 = QPushButton(self.frame_21)
        self.button_15.setObjectName(u"button_15")
        self.button_15.setGeometry(QRect(100, 40, 281, 41))
        self.button_15.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/streamlinehq-common-file-upload-files-folders-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_15.setIcon(icon)
        self.button_15.setIconSize(QSize(25, 25))
        self.button_17 = QPushButton(self.frame_21)
        self.button_17.setObjectName(u"button_17")
        self.button_17.setGeometry(QRect(100, 100, 281, 41))
        self.button_17.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/streamlinehq-webcam-1-computers-devices-electronics-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_17.setIcon(icon1)
        self.button_17.setIconSize(QSize(25, 25))
        self.stacked_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame_12 = QFrame(self.page_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 640, 671, 61))
        self.frame_12.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.button_20 = QPushButton(self.frame_12)
        self.button_20.setObjectName(u"button_20")
        self.button_20.setGeometry(QRect(490, 10, 161, 31))
        self.button_20.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_21 = QPushButton(self.frame_12)
        self.button_21.setObjectName(u"button_21")
        self.button_21.setGeometry(QRect(20, 10, 161, 31))
        self.button_21.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame_8 = QFrame(self.page_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 681, 641))
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 100, 271, 18))
        self.label_8.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 210, 271, 18))
        self.label_9.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(370, 100, 271, 18))
        self.label_10.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(370, 210, 271, 18))
        self.label_11.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 320, 271, 18))
        self.label_12.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.lineEdit_6 = QLineEdit(self.frame_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(70, 130, 231, 31))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.lineEdit_7 = QLineEdit(self.frame_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(370, 130, 231, 31))
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.lineEdit_8 = QLineEdit(self.frame_8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(70, 240, 231, 31))
        self.lineEdit_8.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border-size: 1px;\n"
"	color: #000;\n"
"}")
        self.lineEdit_9 = QLineEdit(self.frame_8)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(370, 240, 231, 31))
        self.lineEdit_9.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.lineEdit_10 = QLineEdit(self.frame_8)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(70, 350, 231, 31))
        self.lineEdit_10.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border-size: 1px;\n"
"	color: #000;\n"
"}")
        self.lineEdit_11 = QLineEdit(self.frame_8)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(370, 350, 231, 31))
        self.lineEdit_11.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border-size: 1px;\n"
"	color: #000;\n"
"}")
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(370, 320, 271, 18))
        self.label_13.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 430, 271, 18))
        self.label_14.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.plainTextEdit = QPlainTextEdit(self.frame_8)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(70, 460, 531, 141))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"	border: 1px solid #8F8F8F;\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}")
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(260, 20, 201, 51))
        self.label_15.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"color: #000;")
        self.stacked_widget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.frame_13 = QFrame(self.page_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 640, 671, 61))
        self.frame_13.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.button_22 = QPushButton(self.frame_13)
        self.button_22.setObjectName(u"button_22")
        self.button_22.setGeometry(QRect(490, 10, 161, 31))
        self.button_22.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_23 = QPushButton(self.frame_13)
        self.button_23.setObjectName(u"button_23")
        self.button_23.setGeometry(QRect(20, 10, 161, 31))
        self.button_23.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 671, 641))
        self.frame_9.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(70, 140, 271, 18))
        self.label_17.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(370, 140, 271, 18))
        self.label_19.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.lineEdit_12 = QLineEdit(self.frame_9)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(70, 170, 231, 31))
        self.lineEdit_12.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.lineEdit_13 = QLineEdit(self.frame_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(370, 170, 231, 31))
        self.lineEdit_13.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(70, 370, 271, 18))
        self.label_23.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_9)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(70, 400, 531, 221))
        self.plainTextEdit_2.setStyleSheet(u"QPlainTextEdit{\n"
"	border: 1px solid #8F8F8F;\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}")
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(230, 20, 241, 51))
        self.label_24.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"color: #000;")
        self.checkBox_2 = QCheckBox(self.frame_9)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(70, 90, 301, 21))
        self.checkBox_2.setStyleSheet(u"color: #f7b733;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.dateEdit_3 = QDateEdit(self.frame_9)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(70, 300, 231, 31))
        self.dateEdit_3.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: #000;")
        self.dateEdit_4 = QDateEdit(self.frame_9)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setGeometry(QRect(370, 300, 231, 31))
        self.dateEdit_4.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: #000;")
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(70, 240, 271, 18))
        self.label_18.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(70, 270, 271, 18))
        self.label_22.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_25 = QLabel(self.frame_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(370, 270, 271, 18))
        self.label_25.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.stacked_widget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.frame_14 = QFrame(self.page_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 640, 671, 61))
        self.frame_14.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.button_24 = QPushButton(self.frame_14)
        self.button_24.setObjectName(u"button_24")
        self.button_24.setGeometry(QRect(490, 10, 161, 31))
        self.button_24.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_25 = QPushButton(self.frame_14)
        self.button_25.setObjectName(u"button_25")
        self.button_25.setGeometry(QRect(20, 10, 161, 31))
        self.button_25.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame = QFrame(self.page_5)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 671, 641))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 100, 271, 18))
        self.label_2.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 210, 271, 18))
        self.label_3.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 100, 271, 18))
        self.label_5.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 210, 271, 18))
        self.label_6.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 320, 271, 18))
        self.label_7.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 130, 231, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(370, 130, 231, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 240, 231, 31))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border-size: 1px;\n"
"	color: #000;\n"
"}")
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(370, 240, 231, 31))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: #000;\n"
"	border-size: 1px;\n"
"}")
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(370, 320, 221, 21))
        self.checkBox.setStyleSheet(u"color: #f7b733;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(70, 380, 231, 31))
        self.dateEdit.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: #000;")
        self.dateEdit_2 = QDateEdit(self.frame)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setEnabled(True)
        self.dateEdit_2.setGeometry(QRect(370, 380, 231, 31))
        self.dateEdit_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: #000;")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(280, 30, 201, 51))
        self.label_16.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"color: #000;")
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(70, 350, 271, 18))
        self.label_20.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(370, 350, 271, 18))
        self.label_21.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.stacked_widget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.frame_15 = QFrame(self.page_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 640, 671, 61))
        self.frame_15.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.button_26 = QPushButton(self.frame_15)
        self.button_26.setObjectName(u"button_26")
        self.button_26.setGeometry(QRect(490, 10, 161, 31))
        self.button_26.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_27 = QPushButton(self.frame_15)
        self.button_27.setObjectName(u"button_27")
        self.button_27.setGeometry(QRect(20, 10, 161, 31))
        self.button_27.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame_23 = QFrame(self.page_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(0, 0, 671, 641))
        self.frame_23.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_27 = QLabel(self.frame_23)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(70, 210, 271, 18))
        self.label_27.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_29 = QLabel(self.frame_23)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(370, 210, 271, 18))
        self.label_29.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_30 = QLabel(self.frame_23)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(70, 290, 271, 18))
        self.label_30.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.lineEdit_16 = QLineEdit(self.frame_23)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(70, 240, 231, 31))
        self.lineEdit_16.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border-size: 1px;\n"
"	color: #000;\n"
"}")
        self.label_31 = QLabel(self.frame_23)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(250, 30, 201, 51))
        self.label_31.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"color: #000;")
        self.listWidget = QListWidget(self.frame_23)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(70, 90, 531, 101))
        self.listWidget.setStyleSheet(u"QListWidget{\n"
"	background-color: #f7b733;\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	font-weight: 600;\n"
"	font-size: 14px;\n"
"	line-height: 65px;\n"
"	text-align: center;\n"
"	letter-spacing: 1px;\n"
"}")
        self.plainTextEdit_3 = QPlainTextEdit(self.frame_23)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(70, 320, 531, 91))
        self.plainTextEdit_3.setStyleSheet(u"QPlainTextEdit{\n"
"	border: 1px solid #8F8F8F;\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}")
        self.button_41 = QPushButton(self.frame_23)
        self.button_41.setObjectName(u"button_41")
        self.button_41.setGeometry(QRect(560, 150, 31, 31))
        self.button_41.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"	border-radius: 5px;\n"
"	color: #fc4a1a;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/streamlinehq-bin-2-interface-essential-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_41.setIcon(icon2)
        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(450, 420, 151, 51))
        self.frame_27.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.button_42 = QPushButton(self.frame_27)
        self.button_42.setObjectName(u"button_42")
        self.button_42.setGeometry(QRect(10, 10, 131, 31))
        self.button_42.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/streamlinehq-add-circle-alternate-interface-essential-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_42.setIcon(icon3)
        self.lineEdit_18 = QLineEdit(self.frame_23)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(370, 240, 231, 31))
        self.lineEdit_18.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border-size: 1px;\n"
"	color: #000;\n"
"}")
        self.stacked_widget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.frame_16 = QFrame(self.page_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 640, 671, 61))
        self.frame_16.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.button_28 = QPushButton(self.frame_16)
        self.button_28.setObjectName(u"button_28")
        self.button_28.setGeometry(QRect(490, 10, 161, 31))
        self.button_28.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_29 = QPushButton(self.frame_16)
        self.button_29.setObjectName(u"button_29")
        self.button_29.setGeometry(QRect(20, 10, 161, 31))
        self.button_29.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame_25 = QFrame(self.page_7)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(0, 0, 671, 641))
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_25)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(190, 210, 271, 18))
        self.label_28.setStyleSheet(u"color: #000;\n"
"font-weight: 600;\n"
"font-size: 17px;")
        self.label_28.setAlignment(Qt.AlignCenter)
        self.lineEdit_17 = QLineEdit(self.frame_25)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(210, 240, 231, 31))
        self.lineEdit_17.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border-size: 1px;\n"
"	color: #000;\n"
"}")
        self.label_34 = QLabel(self.frame_25)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(250, 30, 201, 51))
        self.label_34.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"color: #000;")
        self.listWidget_2 = QListWidget(self.frame_25)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(70, 90, 531, 101))
        self.listWidget_2.setStyleSheet(u"QListWidget{\n"
"	background-color: #f7b733;\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	font-weight: 600;\n"
"	font-size: 14px;\n"
"	line-height: 65px;\n"
"	text-align: center;\n"
"	letter-spacing: 1px;\n"
"}")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(250, 280, 151, 51))
        self.frame_26.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.button_39 = QPushButton(self.frame_26)
        self.button_39.setObjectName(u"button_39")
        self.button_39.setGeometry(QRect(10, 10, 131, 31))
        self.button_39.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_39.setIcon(icon3)
        self.button_40 = QPushButton(self.frame_25)
        self.button_40.setObjectName(u"button_40")
        self.button_40.setGeometry(QRect(560, 150, 31, 31))
        self.button_40.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"	border-radius: 5px;\n"
"	color: #fc4a1a;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_40.setIcon(icon2)
        self.stacked_widget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.frame_17 = QFrame(self.page_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(0, 640, 671, 61))
        self.frame_17.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.button_30 = QPushButton(self.frame_17)
        self.button_30.setObjectName(u"button_30")
        self.button_30.setGeometry(QRect(490, 10, 161, 31))
        self.button_30.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.button_31 = QPushButton(self.frame_17)
        self.button_31.setObjectName(u"button_31")
        self.button_31.setGeometry(QRect(20, 10, 161, 31))
        self.button_31.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.stacked_widget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_4 = QLabel(self.page_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 290, 58, 18))
        self.label_4.setStyleSheet(u"color: #000;")
        self.frame_18 = QFrame(self.page_9)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(0, 640, 671, 61))
        self.frame_18.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.button_32 = QPushButton(self.frame_18)
        self.button_32.setObjectName(u"button_32")
        self.button_32.setGeometry(QRect(20, 10, 161, 31))
        self.button_32.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        self.frame_22 = QFrame(self.page_9)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 0, 671, 641))
        self.frame_22.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 15px;\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.button_33 = QPushButton(self.frame_22)
        self.button_33.setObjectName(u"button_33")
        self.button_33.setGeometry(QRect(230, 280, 221, 41))
        self.button_33.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/streamlinehq-upload-box-internet-networks-servers-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_33.setIcon(icon4)
        self.stacked_widget.addWidget(self.page_9)
        self.side_menu_container = QFrame(self.background_frame)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setGeometry(QRect(0, 0, 231, 701))
        self.side_menu_container.setMinimumSize(QSize(231, 701))
        self.side_menu_container.setMaximumSize(QSize(231, 701))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.side_menu_container.setFont(font)
        self.side_menu_container.setStyleSheet(u"background-color: #4a8dac;\n"
"color: white;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"\n"
"")
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.side_menu_container.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.side_menu_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(self.side_menu_container)
        self.label.setObjectName(u"label")
        self.label.setLineWidth(0)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.frame_1 = QFrame(self.side_menu_container)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setStyleSheet(u"QFrame {border: 0px;}")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.frame_1.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_1)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.frame_6 = QFrame(self.frame_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border-width: 0px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.button_1 = QPushButton(self.frame_6)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")

        self.verticalLayout_11.addWidget(self.button_1)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border-width: 0px;\n"
"border: 0px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.button_2 = QPushButton(self.frame_2)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")

        self.verticalLayout_7.addWidget(self.button_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet(u"background-color: #f7b733;\n"
"font-size: 14px;\n"
"border-width: 0px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.button_4 = QPushButton(self.frame_3)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setEnabled(True)
        self.button_4.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")
        self.button_4.setCheckable(False)
        self.button_4.setChecked(False)

        self.verticalLayout_8.addWidget(self.button_4)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.button_5 = QPushButton(self.frame_3)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_8.addWidget(self.button_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet(u"background-color: #f7b733;\n"
"font-size: 14px;\n"
"border-width: 0px;\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(15, 0, 9, 0)
        self.button_6 = QPushButton(self.frame_7)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_12.addWidget(self.button_6)

        self.button_9 = QPushButton(self.frame_7)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_12.addWidget(self.button_9)

        self.button_10 = QPushButton(self.frame_7)
        self.button_10.setObjectName(u"button_10")
        self.button_10.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_12.addWidget(self.button_10)

        self.button_11 = QPushButton(self.frame_7)
        self.button_11.setObjectName(u"button_11")
        self.button_11.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_12.addWidget(self.button_11)

        self.button_12 = QPushButton(self.frame_7)
        self.button_12.setObjectName(u"button_12")
        self.button_12.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_12.addWidget(self.button_12)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_2)

        self.button_7 = QPushButton(self.frame_3)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_8.addWidget(self.button_7)

        self.line_3 = QFrame(self.frame_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.button_8 = QPushButton(self.frame_3)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_8.addWidget(self.button_8)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-width: 0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.button_3 = QPushButton(self.frame_4)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setStyleSheet(u"QPushButton{\n"
"    background-color: #fc4a1a;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #f24414;\n"
"}")

        self.verticalLayout_9.addWidget(self.button_3)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet(u"background-color: #f7b733;\n"
"font-size: 14px;\n"
"border-width: 0px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.button_231 = QPushButton(self.frame_5)
        self.button_231.setObjectName(u"button_231")
        self.button_231.setStyleSheet(u"QPushButton{\n"
"    background-color: #f7b733;\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: beige;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"}")

        self.verticalLayout_10.addWidget(self.button_231)


        self.verticalLayout_9.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_1)

        self.verticalSpacer = QSpacerItem(20, 637, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.centralWidget)


        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(1)
        self.button_4.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.button_16.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Una herramienta para ayudar a los usuarios a crear y dise\u00f1ar un CV personalizado. La aplicaci\u00f3n permitir\u00e1 a los usuarios seleccionar una plantilla de CV de una variedad de opciones, a\u00f1adir y editar su informaci\u00f3n personal, y exportar el CV en formato PDF para imprimirlo o enviarlo por correo electr\u00f3nico.", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"CV Maker", None))
        self.label_33.setText("")
        self.button_18.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_19.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_35.setText("")
        self.label_36.setText("")
        self.button_15.setText(QCoreApplication.translate("MainWindow", u"Cargar foto", None))
        self.button_17.setText(QCoreApplication.translate("MainWindow", u"Tomar foto", None))
        self.button_20.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_21.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Web", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Perfil Personal", None))
        self.button_22.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_23.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Titulo del trabajo", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Empresa/Compania", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Experiencia Laboral", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"No tengo experiencia laboral", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Periodo", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Desde", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Hasta", None))
        self.button_24.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_25.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre de la institucion", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pais", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Campo de estudio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ciudad", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Periodo", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Estudio actualmente", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Educacion", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Desde", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Hasta", None))
        self.button_26.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_27.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Institucion/Universidad", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Certificaciones", None))
        self.button_41.setText(QCoreApplication.translate("MainWindow", u"''", None))
        self.button_42.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.button_28.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_29.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Habilidad", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Certificaciones", None))
        self.button_39.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.button_40.setText(QCoreApplication.translate("MainWindow", u"''", None))
        self.button_30.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_31.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"pagina 9", None))
        self.button_32.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.button_33.setText(QCoreApplication.translate("MainWindow", u"Exportar CV", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CV Maker", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"Crear CV", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"Cargar Foto", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"Secciones del CV", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"Perfil Personal", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"Experiencia Laboral", None))
        self.button_10.setText(QCoreApplication.translate("MainWindow", u"Educacion", None))
        self.button_11.setText(QCoreApplication.translate("MainWindow", u"Certificaciones", None))
        self.button_12.setText(QCoreApplication.translate("MainWindow", u"Habilidades", None))
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Estilo", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"Exportar CV", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"Editar CV", None))
        self.button_231.setText(QCoreApplication.translate("MainWindow", u"Importar CV", None))
    # retranslateUi

