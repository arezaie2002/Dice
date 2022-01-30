from ast import Num
from concurrent.futures import thread
from typing import Text
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from dice import Ui_MainWindow
import random





class RootMain (QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #..... Btn Connect .....# 
        self.ui.pushButton.clicked.connect(self.dice_core)
        
    

        self.show()

    

    #..... Dice Code .....#
    def dice_core(self):
        num = random.randint(1,6)

        if num == 1:
            self.ui.label_num.setPixmap(QtGui.QPixmap("1.png"))

        elif num ==2:
            self.ui.label_num.setPixmap(QtGui.QPixmap("2.png"))
        
        elif num ==3:
            self.ui.label_num.setPixmap(QtGui.QPixmap("3.png"))

        elif num ==4:
            self.ui.label_num.setPixmap(QtGui.QPixmap("4.png"))

        elif num ==5:
            self.ui.label_num.setPixmap(QtGui.QPixmap("5.png"))

        elif num ==6:
            self.ui.label_num.setPixmap(QtGui.QPixmap("6.png"))

        

    #....... Move With Mouse .......#
    def mousePressEvent(self , evt):
        self.oldpos = evt.globalPos()
    
    def mouseMoveEvent (self , evt) :
        delta = QPoint(evt.globalPos() - self.oldpos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldpos = evt.globalPos()
    


    


if __name__ == '__main__':
    import sys 
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())
    
    