''' author : Du Tang '''

import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, \
    QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5 import QtGui

class Example(QWidget):

    def __init__(self):
        # initialize parent
        super().__init__()
        # initialize self
        self.initUI()

    def initUI(self):
        # set font
        QToolTip.setFont(QFont('SansSerif', 10))

        # set button
        btn = QPushButton('Life is hard', self)
        btn.setToolTip('This is a <b>QPushButton<b> widget')
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # set widget
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Ghost')
        self.setWindowIcon(QIcon('ghost.png'))
        for path in QtGui.QIcon.themeSearchPaths():
            print(path)

        self.show()

    def closeEvent(self, event):
        # reimplement the closeEvent to handle the closeevent
        reply = QMessageBox.question(self, 'Alert', 'Are you sure?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
