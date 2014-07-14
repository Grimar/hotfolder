from PyQt4 import QtGui
import sys
def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    table = QtGui.QTableWidget(5,5,w)
    table.move(0,0)

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
