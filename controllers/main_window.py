import qimage2ndarray
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap

from views.ui_main_window import Ui_MainWindow
from controllers.camera_window import CameraWindowForm

class MainWindowForm(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stacked_widget.setCurrentIndex(0) # Set default init page

        # Init UI element states
        self.frame_3.setVisible(False)
        self.frame_5.setVisible(False)
        self.label_36.setVisible(False)

        # connections
        self.button_1.clicked.connect(self.btn_1)
        self.button_2.clicked.connect(self.btn_2)
        self.button_3.clicked.connect(self.btn_3)
        self.button_4.clicked.connect(lambda: self.change_page(1))
        self.button_5.clicked.connect(lambda: self.change_page(2))
        self.button_6.clicked.connect(lambda: self.change_page(2))
        self.button_7.clicked.connect(lambda: self.change_page(7))
        self.button_8.clicked.connect(lambda: self.change_page(8))
        self.button_9.clicked.connect(lambda: self.change_page(3))
        self.button_10.clicked.connect(lambda: self.change_page(4))
        self.button_11.clicked.connect(lambda: self.change_page(5))
        self.button_12.clicked.connect(lambda: self.change_page(6))
        self.button_16.clicked.connect(lambda: self.change_page(1))
        self.button_18.clicked.connect(lambda: self.change_page(2))
        self.button_19.clicked.connect(lambda: self.change_page(0))
        self.button_20.clicked.connect(lambda: self.change_page(3))
        self.button_21.clicked.connect(lambda: self.change_page(1))
        self.button_22.clicked.connect(lambda: self.change_page(4))
        self.button_23.clicked.connect(lambda: self.change_page(2))
        self.button_24.clicked.connect(lambda: self.change_page(5))
        self.button_25.clicked.connect(lambda: self.change_page(3))
        self.button_26.clicked.connect(lambda: self.change_page(6))
        self.button_27.clicked.connect(lambda: self.change_page(4))
        self.button_28.clicked.connect(lambda: self.change_page(7))
        self.button_29.clicked.connect(lambda: self.change_page(5))
        self.button_30.clicked.connect(lambda: self.change_page(8))
        self.button_31.clicked.connect(lambda: self.change_page(6))
        self.button_32.clicked.connect(lambda: self.change_page(7))
        self.checkBox.toggled.connect(self.cb_1)
        self.checkBox_2.toggled.connect(self.cb_2)
        self.button_40.clicked.connect(self.btn_40)
        self.button_39.clicked.connect(self.btn_39)
        self.button_41.clicked.connect(self.btn_41)
        self.button_42.clicked.connect(self.btn_42)
        self.button_17.clicked.connect(self.open_camera)
        self.button_15.clicked.connect(self.open_file_explorer)

        self.certifications = {}

    def btn_1(self):
        self.stacked_widget.setCurrentIndex(0)
        self.frame_3.setVisible(False)
        self.frame_5.setVisible(False)

    def btn_2(self):
        if self.frame_3.isVisible():
            self.frame_3.setVisible(False)
        else:
            self.frame_3.setVisible(True)
            self.frame_5.setVisible(False)

    def btn_3(self):
        if self.frame_5.isVisible():
            self.frame_5.setVisible(False)
        else:
            self.frame_5.setVisible(True)
            self.frame_3.setVisible(False)

    def change_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

    def cb_1(self):
        if self.checkBox.isChecked():
            self.dateEdit_2.setDisabled(True)
        else:
            self.dateEdit_2.setDisabled(False)

    def cb_2(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_12.setDisabled(True)
            self.lineEdit_13.setDisabled(True)
            self.dateEdit_3.setDisabled(True)
            self.dateEdit_4.setDisabled(True)
            self.plainTextEdit_2.setDisabled(True)
        else:
            self.lineEdit_12.setDisabled(False)
            self.lineEdit_13.setDisabled(False)
            self.dateEdit_3.setDisabled(False)
            self.dateEdit_4.setDisabled(False)
            self.plainTextEdit_2.setDisabled(False)

    def btn_40(self):
        listItems = self.listWidget_2.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.listWidget_2.takeItem(self.listWidget_2.row(item.text()))

    def btn_39(self):
        item = self.lineEdit_17.text()
        if len(item) > 0:
            self.listWidget_2.addItem(item)
            self.lineEdit_17.clear()

    def btn_41(self):
        listItems = self.listWidget.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.certifications.pop(item.text())
            self.listWidget.takeItem(self.listWidget.row(item))

    def btn_42(self):
        item1 = self.lineEdit_16.text()
        item2 = self.lineEdit_18.text()
        item3 = self.plainTextEdit_3.toPlainText()
        if len(item1) > 0 and len(item2) > 0 and len(item3) > 0:
            self.listWidget.addItem(f'{item1} / {item2}')
            self.lineEdit_16.clear()
            self.lineEdit_18.clear()
            self.plainTextEdit_3.clear()
            self.certifications[f'{item1} / {item2}'] = [item1, item2, item3]
        print(self.certifications)

    def open_camera(self):
        self.widget = CameraWindowForm()
        self.widget.bridge = self.set_capture
        self.widget.show()

    def set_capture(self, image):
        self.label_36.setPixmap(QPixmap.fromImage(image))
        self.label_36.setScaledContents(True)
        self.label_36.setVisible(True)

    def open_file_explorer(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', 
        '~/',"Image files (*.jpg *.png *.svg)") #C: \\
        if filename[0] == '':
            return
        imagepath = filename[0]
        pix = QPixmap(imagepath)
        self.label_36.setPixmap(QPixmap(pix))
        self.label_36.setScaledContents(True)
        self.label_36.setVisible(True)

    def save_file_explorer(self):
        pass