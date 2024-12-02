import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPainter, QColor


class LotsOfYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_circles.ui', self)
        self.yellow.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.make_it(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def make_it(self, painter):
        number_of_circkes = random.randint(1, 20)
        for i in range(number_of_circkes):
            diameter = random.randint(1, 200)
            x, y = random.randint(1, 800), random.randint(1, 800)

            painter.setBrush(QColor('yellow'))
            painter.drawEllipse(x, y, diameter, diameter)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = LotsOfYellowCircles()
    ex.show()
    sys.exit(app.exec())
