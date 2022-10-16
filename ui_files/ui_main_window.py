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
    QSizePolicy, QVBoxLayout, QWidget)

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
        self.background_Frame = QFrame(self.centralWidget)
        self.background_Frame.setObjectName(u"background_Frame")
        self.background_Frame.setAutoFillBackground(False)
        self.background_Frame.setStyleSheet(u"background-color: #F4F4F4;")
        self.background_Frame.setFrameShape(QFrame.StyledPanel)
        self.background_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_Frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_content_frame = QFrame(self.background_Frame)
        self.top_content_frame.setObjectName(u"top_content_frame")
        self.top_content_frame.setStyleSheet(u"")
        self.top_content_frame.setFrameShape(QFrame.StyledPanel)
        self.top_content_frame.setFrameShadow(QFrame.Raised)
        self.top_bar_frame = QFrame(self.top_content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setGeometry(QRect(0, 0, 901, 181))
        self.top_bar_frame.setStyleSheet(u"background-color:  rgb(232, 164, 42);")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.top_text_2 = QLabel(self.top_bar_frame)
        self.top_text_2.setObjectName(u"top_text_2")
        self.top_text_2.setGeometry(QRect(240, 20, 411, 71))
        font = QFont()
        font.setFamilies([u"Ubuntu Mono"])
        font.setPointSize(22)
        font.setBold(True)
        self.top_text_2.setFont(font)
        self.top_text_2.setLayoutDirection(Qt.LeftToRight)
        self.top_text_2.setStyleSheet(u"color: rgb(65, 65, 65);")
        self.top_text_2.setAlignment(Qt.AlignCenter)
        self.button_2 = QPushButton(self.top_content_frame)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(380, 380, 131, 71))

        self.verticalLayout_3.addWidget(self.top_content_frame)


        self.verticalLayout_2.addWidget(self.background_Frame)


        self.verticalLayout.addWidget(self.centralWidget)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.top_text_2.setText(QCoreApplication.translate("MainWindow", u"CurriTec", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

