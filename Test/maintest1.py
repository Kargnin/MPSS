import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_GUI_BASE import Ui_MainWindow
import databaseOperations
import CustomModel 

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        self.setWindowTitle('Main Window - Python Base')

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)


        #--------------------------------------
        self.user_data = databaseOperations.get_multiple_data()
        self.model = CustomModel.CustomTableModel(self.user_data)
        self.delegate = CustomModel.InLineEditDelegate()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setItemDelegate(self.delegate)
        # self.ui.tableView.setItemDelegateForColumn(1, self.delegate)
        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.context_menu)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(50)
        self.ui.tableView.setColumnWidth(0, 30)
        self.ui.tableView.hideColumn(0)
        # self.ui.tableView.setModel(self.model)
        # self.ui.tableView.setModel(self.model)

        self.show()

    def context_menu(self):
        menu = QtWidgets.QMenu()
        add_data = menu.addAction("Add New Data")
        add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: self.model.insertRows())
        if self.ui.tableView.selectedIndexes():
            remove_data = menu.addAction("Remove Data")
            remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: self.model.removeRows(self.ui.tableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
