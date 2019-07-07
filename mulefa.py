#!/usr/bin/env python


from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PyQt5.QtGui import QKeySequence, QCursor
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(0)
        self.move(QCursor.pos())
        self.showFullScreen()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Super_L:
            self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    app.exec()
