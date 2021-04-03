import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from Stats import Ui_MainWindow
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
        self.ui.statsTable.setModel(self.model)
        self.ui.statsTable.setItemDelegate(self.delegate)
        # self.ui.statsTable.setItemDelegateForColumn(1, self.delegate)
        # self.ui.statsTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.ui.statsTable.customContextMenuRequested.connect(self.context_menu)
        self.ui.statsTable.verticalHeader().setDefaultSectionSize(50)
        self.ui.statsTable.setColumnWidth(0, 30)
        self.ui.statsTable.hideColumn(0)
        self.ui.statsTable.hideColumn(5)
        
        for i in range(1,5):
            self.ui.statsTable.setColumnWidth(i,214)

        header = self.ui.statsTable.horizontalHeader()  
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        print(self.ui.page_widgets.geometry())

        
        
        # self.ui.statsTable.setModel(self.model)
        # self.ui.statsTable.setModel(self.model)

        self.show()

    # def context_menu(self):
    #     menu = QtWidgets.QMenu()
    #     add_data = menu.addAction("Add New Data")
    #     add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
    #     add_data.triggered.connect(lambda: self.model.insertRows())
    #     if self.ui.statsTable.selectedIndexes():
    #         remove_data = menu.addAction("Remove Data")
    #         remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
    #         remove_data.triggered.connect(lambda: self.model.removeRows(self.ui.statsTable.currentIndex()))
    #     cursor = QtGui.QCursor()
    #     menu.exec_(cursor.pos())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
