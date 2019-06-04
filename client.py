from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
import sys
import hotfolder
from ui import mainwindow, folderDialog
import os.path
import shelve


class HfMain(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(HfMain, self).__init__(parent)
        self.setupUi(self)
        self.folderButton.clicked.connect(self.addFolder)
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = folderDialog.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.folderOpenButton.clicked.connect(self.openFolder)
        self.dialog.ui.buttonBox.accepted.connect(self.openFolderPost)

    @pyqtSlot()
    def addFolder(self):
        self.dialog.show()
        self.dialog.exec_()

    @pyqtSlot()
    def openFolder(self):
        try:
            open_dir = QtWidgets.QFileDialog.getExistingDirectory(
                self,
                "Open a folder",
                os.path.expanduser("~"),
                QtWidgets.QFileDialog.ShowDirsOnly)
            with shelve.open('db') as db:
                db['folderlist'].append(open_dir)
                print(open_dir, db['folderlist'])
                self.dialog.ui.folderEdit.setDuplicatesEnabled(False)
                self.dialog.ui.folderEdit.insertItem(0, open_dir)
                self.dialog.ui.folderEdit.setCurrentIndex(0)
                db.close()
        except ValueError:
            print("Something went wrong")
        self.dialog.raise_()  # put dialog on top

    @pyqtSlot()
    def openFolderPost(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = HfMain()
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
