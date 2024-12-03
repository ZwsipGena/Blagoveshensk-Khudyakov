from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import Qt, QPoint, QPointF
from PyQt6.QtGui import QPainter, QColor
from random import randint
from math import sin, cos, pi


class Suprematism(QWidget):
    def __init__(self):
        self.figure = None
        self.coor = None
        self.flag = False
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.qp = QPainter()

    def mousePressEvent(self, event):
        self.coor = event.pos()
        if event.button() == Qt.MouseButton.LeftButton:
            self.figure = 'circle'
            self.drawf()
        if event.button() == Qt.MouseButton.RightButton:
            self.figure = 'square'
            self.drawf()

    def mouseMoveEvent(self, event):
        self.coor = (event.pos().x(), event.pos().y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.figure = 'triangle'
            self.drawf()

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_figure()
            self.qp.end()

    def draw_figure(self):
        if self.figure == 'circle':
            R = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(QPointF(self.coor.x(), self.coor.y()), R, R)
        elif self.figure == 'square':
            A = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawRect(int(self.coor.x() - A / 2), int(self.coor.y() - A / 2), A, A)
        elif self.figure == 'triangle':
            A = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y = self.coor[0], self.coor[1]
            points = [QPoint(x, y - A),
                      QPoint(int(x + cos(7 * pi / 6) * A),
                             int(y - sin(7 * pi / 6) * A)),
                      QPoint(int(x + cos(11 * pi / 6) * A),
                             int(y - sin(11 * pi / 6) * A))]
            self.qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication([])
    win = Suprematism()
    win.show()
    app.exec()