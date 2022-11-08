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
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 340, 481, 231))
        self.frame.setStyleSheet(u"color: white;\n"
"font-weight: 600;\n"
"font-size: 25px;\n"
"line-height: 65px;\n"
"text-align: center;\n"
"letter-spacing: 1px;\n"
"border: 0px;\n"
"border-radius: 20px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.button_13 = QPushButton(self.frame)
        self.button_13.setObjectName(u"button_13")
        self.button_13.setGeometry(QRect(110, 40, 281, 41))
        self.button_13.setStyleSheet(u"QPushButton{\n"
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
        self.button_14 = QPushButton(self.frame)
        self.button_14.setObjectName(u"button_14")
        self.button_14.setGeometry(QRect(110, 100, 281, 41))
        self.button_14.setStyleSheet(u"QPushButton{\n"
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
        self.frame_8 = QFrame(self.page_1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(100, 90, 481, 251))
        self.frame_8.setStyleSheet(u"border:0px;\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(140, 60, 211, 161))
        self.frame_9.setStyleSheet(u"background-color: #4a8dac;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
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
        self.button_17 = QPushButton(self.frame_10)
        self.button_17.setObjectName(u"button_17")
        self.button_17.setGeometry(QRect(20, 10, 161, 31))
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
        self.stacked_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 290, 241, 41))
        font = QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #000;")
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
        self.stacked_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
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
        self.button_32.setGeometry(QRect(490, 10, 161, 31))
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
        self.button_33 = QPushButton(self.frame_18)
        self.button_33.setObjectName(u"button_33")
        self.button_33.setGeometry(QRect(20, 10, 161, 31))
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
        self.button_13.setText(QCoreApplication.translate("MainWindow", u"Cargar foto", None))
        self.button_14.setText(QCoreApplication.translate("MainWindow", u"Tomar foto", None))
        self.button_16.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_17.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pagina 2", None))
        self.button_18.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_19.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.button_20.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_21.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.button_22.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_23.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.button_24.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_25.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.button_26.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_27.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.button_28.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_29.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.button_30.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_31.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"pagina 9", None))
        self.button_32.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.button_33.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CV Maker", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"Crear CV", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"Cargar Foto", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"Secciones del CV", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"Perfil Personal", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"Experiencia Laboral", None))
        self.button_10.setText(QCoreApplication.translate("MainWindow", u"Certificaciones", None))
        self.button_11.setText(QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.button_12.setText(QCoreApplication.translate("MainWindow", u"Habilidades", None))
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Estilo", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"Exportar CV", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"Editar CV", None))
        self.button_231.setText(QCoreApplication.translate("MainWindow", u"Importar CV", None))
    # retranslateUi

