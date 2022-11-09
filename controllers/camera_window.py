import qimage2ndarray
import cv2
import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap

from views.ui_camera_window import Ui_CameraWindow

class CameraWindowForm(QWidget, Ui_CameraWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_camera()

        self.capture_button.clicked.connect(self.capture_image)

    def setup_camera(self):
        # Iniciar camara
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.image_label.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.image_label.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        # Leer la camara y pintar sobre el qlabel
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        self.image = qimage2ndarray.array2qimage(frame)
        self.image_label.setPixmap(QPixmap.fromImage(self.image))

    def capture_image(self):
        self.bridge(self.image)
        self.close()

    def closeEvent(self, event):
        self.capture.release()
        cv2.destroyAllWindows()
        del self.timer # Importante sin sigue repitiendo
        event.accept()