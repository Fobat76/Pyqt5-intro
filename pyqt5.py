#PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("../pythonProject1/Victini.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0,0,500,500)
        label.setStyleSheet("color: green;")
        label.setAlignment(Qt.AlignHCenter)

        img = QLabel(self)
        img.setGeometry(0,0,250,250)
        pixmap = QPixmap("../pythonProject1/Victini.png")
        img.setPixmap((pixmap))

        img.setScaledContents(True)
        img.setGeometry(self.width() - label.width(),self.height() - img.height(),img.width(),img.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()