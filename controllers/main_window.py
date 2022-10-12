from PySide6.QtWidgets import QWidget

from views.ui_main_window import Ui_MainWindow

class MainWindowForm(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_1.clicked.connect(self.hello)

    def hello(self):
        print('Hello World')