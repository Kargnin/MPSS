# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testyyhqIX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.appContainer = QFrame(self.centralwidget)
        self.appContainer.setObjectName(u"appContainer")
        self.appContainer.setGeometry(QRect(10, 10, 781, 551))
        self.appContainer.setFrameShape(QFrame.StyledPanel)
        self.appContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.appContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableView = QTableView(self.appContainer)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

