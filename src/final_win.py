from inst import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import*

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()