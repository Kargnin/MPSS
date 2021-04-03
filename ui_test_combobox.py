# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_comboboxHSFenC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StatsWindow(object):
    def setupUi(self, StatsWindow):
        if not StatsWindow.objectName():
            StatsWindow.setObjectName(u"StatsWindow")
        StatsWindow.resize(941, 745)
        StatsWindow.setStyleSheet(u"background-color: rgb(34, 40, 49);")
        self.centralwidget = QWidget(StatsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.statsTable = QTableView(self.centralwidget)
        self.statsTable.setObjectName(u"statsTable")
        self.statsTable.setGeometry(QRect(40, 190, 856, 386))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statsTable.sizePolicy().hasHeightForWidth())
        self.statsTable.setSizePolicy(sizePolicy)
        self.statsTable.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.statsTable.setTabletTracking(False)
        self.statsTable.setAutoFillBackground(False)
        self.statsTable.setStyleSheet(u"QTableView {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableView::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.statsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.statsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.statsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.statsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.statsTable.setTabKeyNavigation(True)
        self.statsTable.setProperty("showDropIndicator", False)
        self.statsTable.setDragDropOverwriteMode(False)
        self.statsTable.setSortingEnabled(True)
        self.statsTable.setWordWrap(False)
        self.statsTable.setCornerButtonEnabled(False)
        self.statsTable.verticalHeader().setVisible(False)
        self.statsTable.verticalHeader().setHighlightSections(False)
        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(170, 80, 611, 41))
        self.searchBar.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.searchBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        StatsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(StatsWindow)
        self.statusbar.setObjectName(u"statusbar")
        StatsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatsWindow)

        QMetaObject.connectSlotsByName(StatsWindow)
    # setupUi

    def retranslateUi(self, StatsWindow):
        StatsWindow.setWindowTitle(QCoreApplication.translate("StatsWindow", u"MainWindow", None))
        self.searchBar.setText("")
    # retranslateUi

