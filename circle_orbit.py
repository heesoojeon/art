import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer

import math
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication


def update_position(self):
    print('Updating position...')
    ...

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Circle and Point')

        self.point_pos = [200, 100]  # initial position of the point
        self.angle = 0  # initial angle for the circle

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(1000)  # update every second

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)

        # draw the circle
        pen = QPen(Qt.black, 3)
        qp.setPen(pen)
        qp.drawEllipse(50, 50, 300, 300)

        # draw the point
        pen = QPen(Qt.red, 5)
        qp.setPen(pen)
        qp.drawPoint(*self.point_pos)

    def update_position(self):
        # update the angle of the circle
        self.angle += 10
        if self.angle >= 360:
            self.angle -= 360

        # calculate the new position of the point
        center_x, center_y = 200, 200  # center of the circle
        radius = 150
        x = center_x + radius * (1 + 0.2 * self.angle) * math.cos(math.radians(self.angle))
        y = center_y + radius * (1 + 0.2 * self.angle) * math.sin(math.radians(self.angle))
        self.point_pos = [int(x), int(y)]

        # trigger a repaint of the widget
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())