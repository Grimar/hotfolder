from PyQt5 import QtWidgets, QtGui
import sys
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    table = QtWidgets.QTableWidget(5,5,w)
    table.move(0,0)
    w.setWindowTitle("Hotfolder client 0.1")
    w.setWindowIcon(QtGui.QIcon("icon.png"))
    w.setMinimumSize(400,300)
    table.resize(w.size())

    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

