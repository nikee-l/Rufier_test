from inst import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import*
from final_win import*

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
        self.timer = QLabel(timer_text)
        self.timer.setFont(QFont("Arial", 45))
        self.f_test_btn = QPushButton(f_test_btn_text)
        self.f_test_btn.clicked.connect(self.first_timer_init)
        self.s_test_btn = QPushButton(s_test_btn_text)
        self.thr_test_btn = QPushButton(thr_test_btn_text)
        self.nxt_win_btn = QPushButton(nxt_win_btn_text)
        self.pib_le = QLineEdit(pib_le_text)
        self.years_le = QLineEdit(years_le_text)
        self.f_test_le = QLineEdit(f_test_le_text)
        self.s_test_le = QLineEdit(s_test_le_text)
        self.thr_test_le = QLineEdit(thr_test_le_text)
        #додати віджети у self.h_line
        self.l_line.addWidget(self.pib, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.pib_le, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.years, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.years_le, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.frst_action, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.f_test_btn, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.f_test_le, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.scnd_action, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.s_test_btn, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.thrd_action, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.thr_test_btn, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.s_test_le, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.thr_test_le, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.nxt_win_btn, alignment=Qt.AlignCenter)
        #додати віджет у self.r_line
        self.r_line.addWidget(self.timer, alignment=Qt.AlignRight)
        #додати віджет self.l_line до self.h_line
        self.h_line.addLayout(self.l_line)
        #додати self.r_line до self.h_line
        self.h_line.addLayout(self.r_line)
        #встановити self.h_line основним лейаутом для вікна
        self.setLayout(self.h_line)

    def connects(self):
        self.nxt_win_btn.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.thw = FinalWin()

    def first_timer_init(self):
        global time
        time = QTime(0, 1, 0)
        self.timer_obg = QTimer()
        self.timer_obg.timeout.connect(self.timer1Event)
        self.timer_obg.start(1000)
    
    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss"))
        self.timer.setFont(QFont("Arial", 45, QFont.Bold))
        self.timer.setStyleSheet("color: rgb(36, 100, 227)")
        if time == QTime(0, 0, 0):
            self.timer_obg.stop()
        