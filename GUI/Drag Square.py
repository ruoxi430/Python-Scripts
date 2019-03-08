#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:44:56 2017

@author: Ruoxi Liu 704459374
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog
from PyQt5.QtGui import QPainter, QColor
#from PyQt5.QtCore import QTimer


class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):      
        self.side = 50 
      
        self.old_x = -1
        self.old_y = -1      
        self.x = 0
        self.y = 0
        self.setGeometry(300, 300, 600, 400)
        self.color = QColor(255,0,0)
        self.show()

    def animate(self):
        self.update()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
        qp.setPen(QColor(255, 255, 255, 255))
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, 600, 400)
        
        qp.setPen(self.color)
        qp.setBrush(self.color)
        qp.drawRect(self.x, self.y, self.side, self.side)
        
    def mouseMoveEvent(self, e):
        
        if (self.x <= e.x() <= (self.x + self.side)and 
            self.y <= e.y() <= (self.y + self.side)):
            if self.old_x == -1:
                self.old_x = e.x()
                self.old_y = e.y()
                return;
            self.x = self.x + e.x() - self.old_x
            self.y = self.y + e.y() - self.old_y
            self.old_x = e.x()
            self.old_y = e.y()
            self.update()
        
    def mouseReleaseEvent(self,e):
        self.old_x = -1
        self.old_y = -1 
            
    def mouseDoubleClickEvent (self, e):
        if (self.x <= e.x() <= (self.x + self.side)and 
            self.y <= e.y() <= (self.y + self.side)):
            self.color = QColorDialog.getColor()
            self.update()
        
         
      

            

              
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()