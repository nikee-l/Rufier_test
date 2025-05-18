from inst import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import*

class FinalWin(QWidget):
    def __init__(self, age, t1, t2, t3):
        self.age = int(age)
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
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
        self.description = QLabel(description_text + self.calculate_result())
        self.result_ladel = QLabel(final_result_text + str(self.index))
        self.c_line.addWidget(self.result_ladel, alignment=Qt.AlignCenter)
        self.c_line.addWidget(self.description, alignment=Qt.AlignCenter)
        self.setLayout(self.c_line)

    def calculate_result(self):
        self.index = (4*(int(self.t1) + int(self.t2) + int(self.t3)) - 200)/10
        if self.age >= 15:
            if self.index >= 15:
                return res_low
            elif self.index >= 11:
                return res_ok
            elif self.index >= 6:
                return res_medium
            elif self.index >= 0.5:
                return res_good
            elif self.index < 0.5:
                return res_high
            
        elif self.age >= 13:
            if self.index >= 16.5:
                return res_low
            elif self.index >= 12.5:
                return res_ok
            elif self.index >= 7.5:
                return res_medium
            elif self.index >= 2:
                return res_good
            elif self.index < 2:
                return res_high
        
        elif self.age >= 11:
            if self.index >= 18:
                return res_low
            elif self.index >= 14:
                return res_ok
            elif self.index >= 9:
                return res_medium
            elif self.index >= 3.5:
                return res_good
            elif self.index < 3.5:
                return res_high
            
        elif self.age >= 9:
            if self.index >= 19.5:
                return res_low
            elif self.index >= 15.5:
                return res_ok
            elif self.index >= 10.5:
                return res_medium
            elif self.index >= 5:
                return res_good
            elif self.index < 5:
                return res_high
            
        elif self.age >= 7:
            if self.index >= 21:
                return res_low
            elif self.index >= 17:
                return res_ok
            elif self.index >= 12:
                return res_medium
            elif self.index >= 6.5:
                return res_good
            elif self.index < 6.5:
                return res_high
