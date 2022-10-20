# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

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
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 280, 191, 81))
        font = QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #000;")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 671, 701))
        self.frame.setTabletTracking(False)
        self.frame.setStyleSheet(u"background-color: LightBlue;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 20, 251, 91))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 110, 591, 181))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setMidLineWidth(0)
        self.label_6.setScaledContents(False)
        self.stacked_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 290, 241, 41))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #000;")
        self.stacked_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stacked_widget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stacked_widget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stacked_widget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stacked_widget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stacked_widget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stacked_widget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_4 = QLabel(self.page_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 290, 58, 18))
        self.label_4.setStyleSheet(u"color: #000;")
        self.stacked_widget.addWidget(self.page_9)
        self.side_menu_container = QFrame(self.background_frame)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setGeometry(QRect(0, 0, 231, 701))
        self.side_menu_container.setMinimumSize(QSize(231, 701))
        self.side_menu_container.setMaximumSize(QSize(231, 701))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.side_menu_container.setFont(font1)
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
        self.button_1.setCursor(QCursor(Qt.CrossCursor))
        self.button_1.setFocusPolicy(Qt.ClickFocus)
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
        self.button_1.setAutoRepeatInterval(98)

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
        self.frame_3.setFont(font1)
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
        self.frame_7.setFont(font1)
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
        self.frame_5.setFont(font1)
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

        self.stacked_widget.setCurrentIndex(0)
        self.button_4.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pagina 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:700; color:#0055ff;\">CurriTec</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Muchas veces dise\u00f1ar nuestro Curriculum puede ser algo tedioso<br/>y complicado, es por eso que decidimos crear CurriTec.<br/>Esta aplicaci\u00f3n de escritorio tiene el objetivo de ayudar<br/>a muchas personas, ofreciendo la posibilidad de elegir<br/>entre varias plantillas totalmente gratis y de forma r\u00e1pida.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pagina 2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"pagina 9", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CV Maker", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"Started", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"Create CV", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"Start a New CV", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"Enter CV sections", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"Experience", None))
        self.button_10.setText(QCoreApplication.translate("MainWindow", u"Certifications", None))
        self.button_11.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.button_12.setText(QCoreApplication.translate("MainWindow", u"Skills", None))
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"Select CV Style", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"Select Font Style", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"Edit CV", None))
        self.button_231.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

