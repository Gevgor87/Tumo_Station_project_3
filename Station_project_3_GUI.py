# 1.Please install and activate venv(virtual environment). Steps below (write in terminal)
#       py -m venv venv
#       .\venv\Scripts\activate         for windows
#       source ./venv/bin/activate      for Mac or Linux
# 2.Install PyQt6 library
#       pip install PyQt6

import sys
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSpinBox


#-------------------------------------------------------------------
#                       Window Initialization
#-------------------------------------------------------------------
class Main(QMainWindow):
    def __init__(self) -> None:
        super(Main, self).__init__()

        self.setWindowTitle("Station Project 3")
        self.setGeometry(400,200,460,400)
        self.setWindowIcon(QIcon(".\Images\window_icon.png"))


#-------------------------------------------------------------------
#                       LABELS FOR INPUT
#-------------------------------------------------------------------
        self.hours_text = QLabel(self)
        self.hours_text.setText("Hours")
        self.hours_text.setFont(QFont("Arial", 18))
        self.hours_text.move(65,70)
        self.hours = QSpinBox(self)
        self.hours.setRange(0,24)
        self.hours.move(50,100)

        self.minutes_text = QLabel(self)
        self.minutes_text.setText("Minuts")
        self.minutes_text.setFont(QFont("Arial", 18))
        self.minutes_text.move(195,70)
        self.minutes = QSpinBox(self)
        self.minutes.setRange(0,60)
        self.minutes.move(180,100)

        self.seconds_text = QLabel(self)
        self.seconds_text.setText("Seconds")
        self.seconds_text.setFont(QFont("Arial", 18))
        self.seconds_text.move(310,70)
        self.seconds = QSpinBox(self)
        self.seconds.setRange(0,60)
        self.seconds.setSingleStep(5)
        self.seconds.move(310,100)


#-------------------------------------------------------------------
#                       Button
#-------------------------------------------------------------------
        self.btn = QPushButton(self, text="Start")
        self.btn.setFont(QFont("Arial", 15))
        self.btn.move(180,150)
        self.btn.clicked.connect(self.button_click)

        self.text = QLabel(self)


#-------------------------------------------------------------------
#                   Button click events
#------------------------------------------------------------------- 
    def button_click(self):
        self.time = self.hours.value()*3600 + self.minutes.value()*60 + self.seconds.value()
        self.hours.hide()
        self.hours_text.hide()
        self.minutes.hide()
        self.minutes_text.hide()
        self.seconds.hide()
        self.seconds_text.hide()
        self.btn.hide()
        self.hours_for_print = self.time//3600
        self.minutes_for_print = (self.time-self.hours_for_print*3600)//60
        self.seconds_for_print = self.time-self.hours_for_print*3600-self.minutes_for_print*60
        self.text.setText(f"{self.hours_for_print:02d}:{self.minutes_for_print:02d}:{self.seconds_for_print:02d}")
        self.text.move(180,150)
        self.text.setFont(QFont("Arial", 20))
        self.text.adjustSize()
#-------------------------------------------------------------------
#                     TIMER and funcion
#------------------------------------------------------------------- 
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.counter)

    def counter(self):
        self.time-=1
        self.hours_for_print = self.time//3600
        self.minutes_for_print = (self.time-self.hours_for_print*3600)//60
        self.seconds_for_print = self.time-self.hours_for_print*3600-self.minutes_for_print*60
        self.text.setText(f"{self.hours_for_print:02d}:{self.minutes_for_print:02d}:{self.seconds_for_print:02d}")
        if self.time == 0:
            self.text.setText("Time Over")
            self.text.move(170,150)
            self.text.adjustSize()
            self.text.setStyleSheet('color: red')
            self.timer.stop()


#-------------------------------------------------------------------
#                       RUN WINDOW
#------------------------------------------------------------------- 
def application():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()