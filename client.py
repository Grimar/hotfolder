from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
import sys
import hotfolder
from ui import mainwindow, folderDialog
import os.path


class HfMain(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(HfMain, self).__init__(parent)
        self.setupUi(self)
        self.folderButton.clicked.connect(self.addFolder)

    @pyqtSlot()
    def addFolder(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = folderDialog.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.show()
        self.dialog.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = HfMain()
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
