import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# Example class' base class is widget.
# Note: Python uses (BaseClassName) as substitute for extends BaseClassName in Java.
class OffPodGUI(QWidget):

    # Constructor is defined as the function __init__(self), with (self) being the base class name.
    def __init__(self):
        super().__init__()
        self.title = 'Spartan Hyperloop'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 880
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('web.png'))

        stop_button = QPushButton('STOP', self)
        stop_button.move(100, 100)
        stop_button.setToolTip('Emergency Stop')
        stop_button.clicked.connect(lambda: self.emergencyQuit())
        stop_button.show()
        self.show()

    def emergencyQuit(self):
        print('stopping')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OffPodGUI()
    sys.exit(app.exec_())
