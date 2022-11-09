# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_window.ui'
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
    QSizePolicy, QWidget)

class Ui_CameraWindow(object):
    def setupUi(self, CameraWindow):
        if not CameraWindow.objectName():
            CameraWindow.setObjectName(u"CameraWindow")
        CameraWindow.resize(582, 474)
        CameraWindow.setMinimumSize(QSize(582, 474))
        CameraWindow.setMaximumSize(QSize(582, 474))
        self.background_frame = QFrame(CameraWindow)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setGeometry(QRect(-50, -10, 651, 531))
        self.background_frame.setAutoFillBackground(False)
        self.background_frame.setStyleSheet(u"background-color: #4a8dac;")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.background_frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(40, 10, 591, 471))
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	border:0px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(10, 420, 581, 51))
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
        self.capture_button = QPushButton(self.frame_26)
        self.capture_button.setObjectName(u"capture_button")
        self.capture_button.setGeometry(QRect(410, 10, 131, 31))
        self.capture_button.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"./assets/icons/streamlinehq-camera-images-photography-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.capture_button.setIcon(icon)
        self.frame = QFrame(self.frame_25)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 541, 401))
        self.frame.setStyleSheet(u"background-color: #F4F4F4;\n"
"border-radius: 16px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.image_label = QLabel(self.frame)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(10, 10, 521, 381))
        self.image_label.setStyleSheet(u"border-radius: 15px;")

        self.retranslateUi(CameraWindow)

        QMetaObject.connectSlotsByName(CameraWindow)
    # setupUi

    def retranslateUi(self, CameraWindow):
        CameraWindow.setWindowTitle(QCoreApplication.translate("CameraWindow", u"Camara", None))
        self.capture_button.setText(QCoreApplication.translate("CameraWindow", u"Capturar", None))
        self.image_label.setText("")
    # retranslateUi

