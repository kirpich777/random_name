import sys
import random
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPainter, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.yellow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.yellow.setGeometry(QtCore.QRect(350, 370, 141, 41))
        self.yellow.setObjectName("yellow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yellow.setText(_translate("MainWindow", "Pushhhh"))


class LotsOfYellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            painter.setBrush(QColor(r, g, b))
            painter.drawEllipse(x, y, diameter, diameter)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = LotsOfYellowCircles()
    ex.show()
    sys.exit(app.exec())
