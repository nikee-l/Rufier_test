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

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.c_line = QVBoxLayout()
        self.result_ladel = QLabel(final_result_text)
        self.description = QLabel(description_text)
        self.c_line.addWidget(self.result_ladel, alignment=Qt.AlignCenter)
        self.c_line.addWidget(self.description, alignment=Qt.AlignCenter)
        self.setLayout(self.c_line)