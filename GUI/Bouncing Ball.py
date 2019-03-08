import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer


class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):      
        self.d = 30
        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 1
      
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(3)
                
        self.setGeometry(300, 300, 600, 400)

        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
        qp.setPen(QColor(255, 255, 255, 255))
          
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())
        
        qp.setPen(QColor(255, 0, 0, 255))
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)
      
    def animate(self):
            self.x += self.dx
            self.y += self.dy
            self.checkCollision()
            self.update()

        
    def checkCollision(self):
        if self.height() <= self.d*2 or self.width()<= self.d*2:
            self.resize(self.d*2, self.d*2)
        if (self.x <= 0):
            self.dx = -self.dx
        elif (self.x + self.d) >= self.width():
            self.dx = -self.dx
            self.x = self.width() - self.d
        if (self.y <= 0):
            self.dy = -self.dy
        elif (self.y + self.d)>= self.height():
            self.dy = -self.dy
            self.y = self.height() - self.d
            

              
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()