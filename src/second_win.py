from inst import*
from PyQt5.QtWidgets import*
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title2)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.pib = QLabel(pib_text)
        self.years = QLabel(years_text)
        self.frst_action = QLabel(frst_action_text)
        self.scnd_action = QLabel(scnd_action_text)
        self.thrd_action = QLabel(thrd_action_text)
        self.timer = QLabel()
        self.f_test_btn = QPushButton(f_test_btn_text)
        self.s_test_btn = QPushButton(s_test_btn_text)
        self.thr_test_btn = QPushButton(thr_test_btn_text)
        self.nxt_win_btn = QPushButton(nxt_win_btn_text)
        self.pib_le = QLineEdit(pib_le_text)
        self.years_le = QLineEdit(years_le_text)
        self.f_test_le = QLineEdit(f_test_le_text)
        self.s_test_le = QLineEdit(s_test_le_text)
        self.thr_test_le = QLineEdit(thr_test_le_text)
        #додати віджети у self.h_line
        self.r_line.addWidget(self.pib)
        self.r_line.addWidget(self.years)
        self.r_line.addWidget(self.frst_action)
        self.r_line.addWidget(self.scnd_action)
        self.r_line.addWidget(self.thrd_action)
        # self.h_line.addWidget(f_test_btn_text)
        # self.h_line.addWidget(s_test_btn_text)
        # self.h_line.addWidget(thr_test_btn_text)
        # self.h_line.addWidget(nxt_win_btn_text)
        # self.h_line.addWidget(pib_le_text)
        # self.h_line.addWidget(years_le_text)
        # self.h_line.addWidget(f_test_le_text)
        # self.h_line.addWidget(s_test_le_text)
        # self.h_line.addWidget(thr_test_le)
        #додати віджет у self.r_line
        #додати віджет self.l_line до self.h_line
        #додати self.r_line до self.h_line
        #встановити self.h_line основним лейаутом для вікна
        self.setLayout(self.r_line)

    def connects(self):
        pass