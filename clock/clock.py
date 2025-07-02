import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPainter,QBrush,QColor,QPen,QPixmap,QFont
from PyQt5.QtCore import Qt,QTimer,QRect
import datetime
from time import sleep

class Window(QMainWindow):
    def __init__(self,text_f,font_size=90):
        super().__init__()
        self.setGeometry(0,0,QApplication.desktop().screenGeometry().width(),QApplication.desktop().screenGeometry().height())
        self.setAttribute(Qt.WA_TranslucentBackground,True)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.text=text_f
        self.label=QLabel(self)
        self.font=QFont()
        self.font.setPointSize(font_size)
        self.label.setFont(self.font)
        color=QColor(128,128,128,128)
        self.label.setStyleSheet(f'color: rgba({color.red()}, {color.green()}, {color.blue()}, {color.alpha()});')
        self.label.resize(int(font_size*3.5),font_size*2)#3.5,  2 коэффициенты
    def move(self,coordinates=(0,0)):
        self.label.move(*coordinates)
    def paintEvent(self,event):
        self.label.setText(self.text())
        QTimer.singleShot(1000, self.update)
###
if __name__ == "__main__":
    main=True
    def time():
        current_time=datetime.datetime.now()
        hour= '' if len(str(current_time.hour))>1 else '0'
        minute= '' if len(str(current_time.minute))>1 else '0'
        hour+=str(current_time.hour)
        minute+=str(current_time.minute)
        return f"{hour}:{minute}"
    app=QApplication(sys.argv)
    window=Window(time)
    window.show()
    print(1)
    window.move((100,100))
    print(2)
    '''
    while main:
        inp=input()
        if inp=='':
            main=False
        print(3)'''
    sys.exit(app.exec_())
    print(4)

