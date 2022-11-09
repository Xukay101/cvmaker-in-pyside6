from PySide6.QtWidgets import QWidget

from views.ui_main_window import Ui_MainWindow

class MainWindowForm(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.stacked_widget.setCurrentIndex(0) # Set default init page

        self.stacked_widget.setCurrentIndex(0) # Set default init page

        # Init UI element states
        self.frame_3.setVisible(False)
        self.frame_5.setVisible(False)

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

<<<<<<< HEAD
    def change_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
=======
    def btn_4(self):
        self.stacked_widget.setCurrentIndex(1)

    def btn_5(self):
        pass

    def btn_6(self):
        self.stacked_widget.setCurrentIndex(2)

    def btn_7(self):
        self.stacked_widget.setCurrentIndex(7)

    def btn_8(self):
        self.stacked_widget.setCurrentIndex(8)

    def btn_9(self):
        self.stacked_widget.setCurrentIndex(3)

    def btn_10(self):
        self.stacked_widget.setCurrentIndex(4)

    def btn_11(self):
        self.stacked_widget.setCurrentIndex(5)

    def btn_12(self):
        self.stacked_widget.setCurrentIndex(6)
>>>>>>> d9927abcbcfdc65d23694a959f974f1d3798caa5
