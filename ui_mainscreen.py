# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainscreenaTiYqf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush15 = QBrush(QColor(210, 210, 210, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.stackedWidget.setPalette(palette1)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_8 = QVBoxLayout(self.page_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(40)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(17)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(14)
        self.label_7.setFont(font7)
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_sell = QWidget()
        self.page_sell.setObjectName(u"page_sell")
        self.verticalLayout_13 = QVBoxLayout(self.page_sell)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sell_title_label = QLabel(self.page_sell)
        self.sell_title_label.setObjectName(u"sell_title_label")
        sizePolicy5.setHeightForWidth(self.sell_title_label.sizePolicy().hasHeightForWidth())
        self.sell_title_label.setSizePolicy(sizePolicy5)
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(20)
        self.sell_title_label.setFont(font8)
        self.sell_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.sell_title_label)

        self.sell_Table = QTableView(self.page_sell)
        self.sell_Table.setObjectName(u"sell_Table")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sell_Table.sizePolicy().hasHeightForWidth())
        self.sell_Table.setSizePolicy(sizePolicy6)
        self.sell_Table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.sell_Table.setTabletTracking(False)
        self.sell_Table.setAutoFillBackground(False)
        self.sell_Table.setStyleSheet(u"QTableView {	\n"
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
        self.sell_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sell_Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sell_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sell_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sell_Table.setTabKeyNavigation(True)
        self.sell_Table.setProperty("showDropIndicator", False)
        self.sell_Table.setDragDropOverwriteMode(False)
        self.sell_Table.setSortingEnabled(True)
        self.sell_Table.setWordWrap(False)
        self.sell_Table.setCornerButtonEnabled(False)
        self.sell_Table.verticalHeader().setVisible(False)
        self.sell_Table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_13.addWidget(self.sell_Table)

        self.frame_9 = QFrame(self.page_sell)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy5.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy5)
        self.frame_9.setFont(font2)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.sell_addBtn = QPushButton(self.frame_9)
        self.sell_addBtn.setObjectName(u"sell_addBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.sell_addBtn.sizePolicy().hasHeightForWidth())
        self.sell_addBtn.setSizePolicy(sizePolicy7)
        self.sell_addBtn.setFont(font)
        self.sell_addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sell_addBtn.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.sell_addBtn)

        self.sell_removeBtn = QPushButton(self.frame_9)
        self.sell_removeBtn.setObjectName(u"sell_removeBtn")
        sizePolicy7.setHeightForWidth(self.sell_removeBtn.sizePolicy().hasHeightForWidth())
        self.sell_removeBtn.setSizePolicy(sizePolicy7)
        self.sell_removeBtn.setFont(font)
        self.sell_removeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sell_removeBtn.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.sell_removeBtn)

        self.sell_finishBtn = QPushButton(self.frame_9)
        self.sell_finishBtn.setObjectName(u"sell_finishBtn")
        sizePolicy7.setHeightForWidth(self.sell_finishBtn.sizePolicy().hasHeightForWidth())
        self.sell_finishBtn.setSizePolicy(sizePolicy7)
        self.sell_finishBtn.setFont(font)
        self.sell_finishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sell_finishBtn.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.sell_finishBtn)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page_sell)
        self.page_sell_select = QWidget()
        self.page_sell_select.setObjectName(u"page_sell_select")
        self.verticalLayout_10 = QVBoxLayout(self.page_sell_select)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sell_select_title_label = QLabel(self.page_sell_select)
        self.sell_select_title_label.setObjectName(u"sell_select_title_label")
        sizePolicy5.setHeightForWidth(self.sell_select_title_label.sizePolicy().hasHeightForWidth())
        self.sell_select_title_label.setSizePolicy(sizePolicy5)
        self.sell_select_title_label.setFont(font8)
        self.sell_select_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.sell_select_title_label)

        self.sell_select_containerframe = QFrame(self.page_sell_select)
        self.sell_select_containerframe.setObjectName(u"sell_select_containerframe")
        sizePolicy5.setHeightForWidth(self.sell_select_containerframe.sizePolicy().hasHeightForWidth())
        self.sell_select_containerframe.setSizePolicy(sizePolicy5)
        self.sell_select_containerframe.setFont(font2)
        self.sell_select_containerframe.setFrameShape(QFrame.StyledPanel)
        self.sell_select_containerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.sell_select_containerframe)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.choiceLabel = QLabel(self.sell_select_containerframe)
        self.choiceLabel.setObjectName(u"choiceLabel")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setWeight(50)
        self.choiceLabel.setFont(font9)
        self.choiceLabel.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.choiceLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.choiceLabel)

        self.sell_select_choiceBox = QComboBox(self.sell_select_containerframe)
        self.sell_select_choiceBox.setObjectName(u"sell_select_choiceBox")
        self.sell_select_choiceBox.setFont(font2)
        self.sell_select_choiceBox.setStyleSheet(u"color: rgb(236, 236, 236);")

        self.horizontalLayout_9.addWidget(self.sell_select_choiceBox)


        self.verticalLayout_10.addWidget(self.sell_select_containerframe)

        self.sell_select_searchBar = QLineEdit(self.page_sell_select)
        self.sell_select_searchBar.setObjectName(u"sell_select_searchBar")
        self.sell_select_searchBar.setFont(font)
        self.sell_select_searchBar.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.sell_select_searchBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.sell_select_searchBar)

        self.sell_select_Table = QTableView(self.page_sell_select)
        self.sell_select_Table.setObjectName(u"sell_select_Table")
        sizePolicy6.setHeightForWidth(self.sell_select_Table.sizePolicy().hasHeightForWidth())
        self.sell_select_Table.setSizePolicy(sizePolicy6)
        self.sell_select_Table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.sell_select_Table.setTabletTracking(False)
        self.sell_select_Table.setAutoFillBackground(False)
        self.sell_select_Table.setStyleSheet(u"QTableView {	\n"
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
        self.sell_select_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sell_select_Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sell_select_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sell_select_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sell_select_Table.setTabKeyNavigation(True)
        self.sell_select_Table.setProperty("showDropIndicator", False)
        self.sell_select_Table.setDragDropOverwriteMode(False)
        self.sell_select_Table.setSortingEnabled(True)
        self.sell_select_Table.setWordWrap(False)
        self.sell_select_Table.setCornerButtonEnabled(False)
        self.sell_select_Table.verticalHeader().setVisible(False)
        self.sell_select_Table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_10.addWidget(self.sell_select_Table)

        self.frame = QFrame(self.page_sell_select)
        self.frame.setObjectName(u"frame")
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.sell_select_volLabel = QLabel(self.frame)
        self.sell_select_volLabel.setObjectName(u"sell_select_volLabel")
        self.sell_select_volLabel.setFont(font9)
        self.sell_select_volLabel.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.sell_select_volLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.sell_select_volLabel)

        self.sell_select_volEdit = QLineEdit(self.frame)
        self.sell_select_volEdit.setObjectName(u"sell_select_volEdit")
        sizePolicy5.setHeightForWidth(self.sell_select_volEdit.sizePolicy().hasHeightForWidth())
        self.sell_select_volEdit.setSizePolicy(sizePolicy5)
        self.sell_select_volEdit.setFont(font)
        self.sell_select_volEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.sell_select_volEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.sell_select_volEdit)

        self.sell_select_priceLabel = QLabel(self.frame)
        self.sell_select_priceLabel.setObjectName(u"sell_select_priceLabel")
        self.sell_select_priceLabel.setFont(font9)
        self.sell_select_priceLabel.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.sell_select_priceLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.sell_select_priceLabel)

        self.sell_select_priceEdit = QLineEdit(self.frame)
        self.sell_select_priceEdit.setObjectName(u"sell_select_priceEdit")
        sizePolicy5.setHeightForWidth(self.sell_select_priceEdit.sizePolicy().hasHeightForWidth())
        self.sell_select_priceEdit.setSizePolicy(sizePolicy5)
        self.sell_select_priceEdit.setFont(font)
        self.sell_select_priceEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.sell_select_priceEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.sell_select_priceEdit)


        self.verticalLayout_10.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_sell_select)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setFont(font2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sell_select_addBtn = QPushButton(self.frame_2)
        self.sell_select_addBtn.setObjectName(u"sell_select_addBtn")
        sizePolicy7.setHeightForWidth(self.sell_select_addBtn.sizePolicy().hasHeightForWidth())
        self.sell_select_addBtn.setSizePolicy(sizePolicy7)
        self.sell_select_addBtn.setFont(font)
        self.sell_select_addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sell_select_addBtn.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.sell_select_addBtn)

        self.sell_select_finishBtn = QPushButton(self.frame_2)
        self.sell_select_finishBtn.setObjectName(u"sell_select_finishBtn")
        sizePolicy7.setHeightForWidth(self.sell_select_finishBtn.sizePolicy().hasHeightForWidth())
        self.sell_select_finishBtn.setSizePolicy(sizePolicy7)
        self.sell_select_finishBtn.setFont(font)
        self.sell_select_finishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sell_select_finishBtn.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.sell_select_finishBtn)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_sell_select)
        self.page_buy = QWidget()
        self.page_buy.setObjectName(u"page_buy")
        self.verticalLayout_14 = QVBoxLayout(self.page_buy)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.buy_title_label = QLabel(self.page_buy)
        self.buy_title_label.setObjectName(u"buy_title_label")
        sizePolicy5.setHeightForWidth(self.buy_title_label.sizePolicy().hasHeightForWidth())
        self.buy_title_label.setSizePolicy(sizePolicy5)
        self.buy_title_label.setFont(font8)
        self.buy_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.buy_title_label)

        self.buy_Table = QTableView(self.page_buy)
        self.buy_Table.setObjectName(u"buy_Table")
        sizePolicy6.setHeightForWidth(self.buy_Table.sizePolicy().hasHeightForWidth())
        self.buy_Table.setSizePolicy(sizePolicy6)
        self.buy_Table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.buy_Table.setTabletTracking(False)
        self.buy_Table.setAutoFillBackground(False)
        self.buy_Table.setStyleSheet(u"QTableView {	\n"
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
        self.buy_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.buy_Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.buy_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.buy_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.buy_Table.setTabKeyNavigation(True)
        self.buy_Table.setProperty("showDropIndicator", False)
        self.buy_Table.setDragDropOverwriteMode(False)
        self.buy_Table.setSortingEnabled(True)
        self.buy_Table.setWordWrap(False)
        self.buy_Table.setCornerButtonEnabled(False)
        self.buy_Table.verticalHeader().setVisible(False)
        self.buy_Table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_14.addWidget(self.buy_Table)

        self.frame_10 = QFrame(self.page_buy)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy5.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy5)
        self.frame_10.setFont(font2)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.buy_addBtn = QPushButton(self.frame_10)
        self.buy_addBtn.setObjectName(u"buy_addBtn")
        sizePolicy7.setHeightForWidth(self.buy_addBtn.sizePolicy().hasHeightForWidth())
        self.buy_addBtn.setSizePolicy(sizePolicy7)
        self.buy_addBtn.setFont(font)
        self.buy_addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_addBtn.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.buy_addBtn)

        self.buy_removeBtn = QPushButton(self.frame_10)
        self.buy_removeBtn.setObjectName(u"buy_removeBtn")
        sizePolicy7.setHeightForWidth(self.buy_removeBtn.sizePolicy().hasHeightForWidth())
        self.buy_removeBtn.setSizePolicy(sizePolicy7)
        self.buy_removeBtn.setFont(font)
        self.buy_removeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_removeBtn.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.buy_removeBtn)

        self.buy_orderBtn = QPushButton(self.frame_10)
        self.buy_orderBtn.setObjectName(u"buy_orderBtn")
        sizePolicy7.setHeightForWidth(self.buy_orderBtn.sizePolicy().hasHeightForWidth())
        self.buy_orderBtn.setSizePolicy(sizePolicy7)
        self.buy_orderBtn.setFont(font)
        self.buy_orderBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_orderBtn.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.buy_orderBtn)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_buy)
        self.page_buy_select = QWidget()
        self.page_buy_select.setObjectName(u"page_buy_select")
        self.page_buy_select.setFont(font2)
        self.verticalLayout_11 = QVBoxLayout(self.page_buy_select)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.buy_select_title_label = QLabel(self.page_buy_select)
        self.buy_select_title_label.setObjectName(u"buy_select_title_label")
        sizePolicy5.setHeightForWidth(self.buy_select_title_label.sizePolicy().hasHeightForWidth())
        self.buy_select_title_label.setSizePolicy(sizePolicy5)
        self.buy_select_title_label.setFont(font8)
        self.buy_select_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.buy_select_title_label)

        self.frame_3 = QFrame(self.page_buy_select)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.choiceLabel_2 = QLabel(self.frame_3)
        self.choiceLabel_2.setObjectName(u"choiceLabel_2")
        self.choiceLabel_2.setFont(font9)
        self.choiceLabel_2.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.choiceLabel_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.choiceLabel_2)

        self.buy_select_choiceBox = QComboBox(self.frame_3)
        self.buy_select_choiceBox.setObjectName(u"buy_select_choiceBox")
        self.buy_select_choiceBox.setFont(font2)
        self.buy_select_choiceBox.setStyleSheet(u"color: rgb(236, 236, 236);")

        self.horizontalLayout_13.addWidget(self.buy_select_choiceBox)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.buy_select_searchBar = QLineEdit(self.page_buy_select)
        self.buy_select_searchBar.setObjectName(u"buy_select_searchBar")
        self.buy_select_searchBar.setFont(font)
        self.buy_select_searchBar.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.buy_select_searchBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.buy_select_searchBar)

        self.buy_select_Table = QTableView(self.page_buy_select)
        self.buy_select_Table.setObjectName(u"buy_select_Table")
        sizePolicy6.setHeightForWidth(self.buy_select_Table.sizePolicy().hasHeightForWidth())
        self.buy_select_Table.setSizePolicy(sizePolicy6)
        self.buy_select_Table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.buy_select_Table.setTabletTracking(False)
        self.buy_select_Table.setAutoFillBackground(False)
        self.buy_select_Table.setStyleSheet(u"QTableView {	\n"
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
        self.buy_select_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.buy_select_Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.buy_select_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.buy_select_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.buy_select_Table.setTabKeyNavigation(True)
        self.buy_select_Table.setProperty("showDropIndicator", False)
        self.buy_select_Table.setDragDropOverwriteMode(False)
        self.buy_select_Table.setSortingEnabled(True)
        self.buy_select_Table.setWordWrap(False)
        self.buy_select_Table.setCornerButtonEnabled(False)
        self.buy_select_Table.verticalHeader().setVisible(False)
        self.buy_select_Table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_11.addWidget(self.buy_select_Table)

        self.frame_4 = QFrame(self.page_buy_select)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.buy_select_volLabel = QLabel(self.frame_4)
        self.buy_select_volLabel.setObjectName(u"buy_select_volLabel")
        self.buy_select_volLabel.setFont(font9)
        self.buy_select_volLabel.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.buy_select_volLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.buy_select_volLabel)

        self.buy_select_volEdit = QLineEdit(self.frame_4)
        self.buy_select_volEdit.setObjectName(u"buy_select_volEdit")
        sizePolicy5.setHeightForWidth(self.buy_select_volEdit.sizePolicy().hasHeightForWidth())
        self.buy_select_volEdit.setSizePolicy(sizePolicy5)
        self.buy_select_volEdit.setFont(font)
        self.buy_select_volEdit.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.buy_select_volEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.buy_select_volEdit)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.page_buy_select)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
        self.frame_5.setFont(font2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.buy_select_addBtn = QPushButton(self.frame_5)
        self.buy_select_addBtn.setObjectName(u"buy_select_addBtn")
        sizePolicy7.setHeightForWidth(self.buy_select_addBtn.sizePolicy().hasHeightForWidth())
        self.buy_select_addBtn.setSizePolicy(sizePolicy7)
        self.buy_select_addBtn.setFont(font)
        self.buy_select_addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_select_addBtn.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.buy_select_addBtn)

        self.buy_select_finishBtn = QPushButton(self.frame_5)
        self.buy_select_finishBtn.setObjectName(u"buy_select_finishBtn")
        sizePolicy7.setHeightForWidth(self.buy_select_finishBtn.sizePolicy().hasHeightForWidth())
        self.buy_select_finishBtn.setSizePolicy(sizePolicy7)
        self.buy_select_finishBtn.setFont(font)
        self.buy_select_finishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_select_finishBtn.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.buy_select_finishBtn)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_buy_select)
        self.page_add_remove = QWidget()
        self.page_add_remove.setObjectName(u"page_add_remove")
        self.verticalLayout_15 = QVBoxLayout(self.page_add_remove)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.add_remove_title_label = QLabel(self.page_add_remove)
        self.add_remove_title_label.setObjectName(u"add_remove_title_label")
        sizePolicy5.setHeightForWidth(self.add_remove_title_label.sizePolicy().hasHeightForWidth())
        self.add_remove_title_label.setSizePolicy(sizePolicy5)
        self.add_remove_title_label.setFont(font8)
        self.add_remove_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.add_remove_title_label)

        self.frame_11 = QFrame(self.page_add_remove)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy5.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy5)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.choiceLabel_3 = QLabel(self.frame_11)
        self.choiceLabel_3.setObjectName(u"choiceLabel_3")
        self.choiceLabel_3.setFont(font9)
        self.choiceLabel_3.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.choiceLabel_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.choiceLabel_3)

        self.add_remove_choiceBox = QComboBox(self.frame_11)
        self.add_remove_choiceBox.setObjectName(u"add_remove_choiceBox")
        self.add_remove_choiceBox.setFont(font2)
        self.add_remove_choiceBox.setStyleSheet(u"color: rgb(236, 236, 236);")

        self.horizontalLayout_21.addWidget(self.add_remove_choiceBox)


        self.verticalLayout_15.addWidget(self.frame_11)

        self.add_remove_searchBar = QLineEdit(self.page_add_remove)
        self.add_remove_searchBar.setObjectName(u"add_remove_searchBar")
        self.add_remove_searchBar.setFont(font)
        self.add_remove_searchBar.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.add_remove_searchBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.add_remove_searchBar)

        self.add_remove_Table = QTableView(self.page_add_remove)
        self.add_remove_Table.setObjectName(u"add_remove_Table")
        sizePolicy6.setHeightForWidth(self.add_remove_Table.sizePolicy().hasHeightForWidth())
        self.add_remove_Table.setSizePolicy(sizePolicy6)
        self.add_remove_Table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.add_remove_Table.setTabletTracking(False)
        self.add_remove_Table.setAutoFillBackground(False)
        self.add_remove_Table.setStyleSheet(u"QTableView {	\n"
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
        self.add_remove_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.add_remove_Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.add_remove_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.add_remove_Table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.add_remove_Table.setTabKeyNavigation(True)
        self.add_remove_Table.setProperty("showDropIndicator", False)
        self.add_remove_Table.setDragDropOverwriteMode(False)
        self.add_remove_Table.setSortingEnabled(True)
        self.add_remove_Table.setWordWrap(False)
        self.add_remove_Table.setCornerButtonEnabled(False)
        self.add_remove_Table.verticalHeader().setVisible(False)
        self.add_remove_Table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_15.addWidget(self.add_remove_Table)

        self.frame_12 = QFrame(self.page_add_remove)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy5.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy5)
        self.frame_12.setFont(font2)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.add_remove_addBtn = QPushButton(self.frame_12)
        self.add_remove_addBtn.setObjectName(u"add_remove_addBtn")
        sizePolicy7.setHeightForWidth(self.add_remove_addBtn.sizePolicy().hasHeightForWidth())
        self.add_remove_addBtn.setSizePolicy(sizePolicy7)
        self.add_remove_addBtn.setFont(font)
        self.add_remove_addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_remove_addBtn.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.add_remove_addBtn)

        self.add_remove_removeBtn = QPushButton(self.frame_12)
        self.add_remove_removeBtn.setObjectName(u"add_remove_removeBtn")
        sizePolicy7.setHeightForWidth(self.add_remove_removeBtn.sizePolicy().hasHeightForWidth())
        self.add_remove_removeBtn.setSizePolicy(sizePolicy7)
        self.add_remove_removeBtn.setFont(font)
        self.add_remove_removeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_remove_removeBtn.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.add_remove_removeBtn)

        self.add_remove_modifylistBtn = QPushButton(self.frame_12)
        self.add_remove_modifylistBtn.setObjectName(u"add_remove_modifylistBtn")
        sizePolicy7.setHeightForWidth(self.add_remove_modifylistBtn.sizePolicy().hasHeightForWidth())
        self.add_remove_modifylistBtn.setSizePolicy(sizePolicy7)
        self.add_remove_modifylistBtn.setFont(font)
        self.add_remove_modifylistBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_remove_modifylistBtn.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.add_remove_modifylistBtn)


        self.verticalLayout_15.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page_add_remove)
        self.page_modifylist = QWidget()
        self.page_modifylist.setObjectName(u"page_modifylist")
        self.verticalLayout_16 = QVBoxLayout(self.page_modifylist)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.modifylist_title_label = QLabel(self.page_modifylist)
        self.modifylist_title_label.setObjectName(u"modifylist_title_label")
        sizePolicy5.setHeightForWidth(self.modifylist_title_label.sizePolicy().hasHeightForWidth())
        self.modifylist_title_label.setSizePolicy(sizePolicy5)
        self.modifylist_title_label.setFont(font8)
        self.modifylist_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.modifylist_title_label)

        self.modifylist_Table_2 = QTableView(self.page_modifylist)
        self.modifylist_Table_2.setObjectName(u"modifylist_Table_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.modifylist_Table_2.sizePolicy().hasHeightForWidth())
        self.modifylist_Table_2.setSizePolicy(sizePolicy8)
        self.modifylist_Table_2.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.modifylist_Table_2.setTabletTracking(False)
        self.modifylist_Table_2.setAutoFillBackground(False)
        self.modifylist_Table_2.setStyleSheet(u"QTableView {	\n"
"	background-color: transparent;\n"
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
"	Background-color:transparent;\n"
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
"	background-color: transparent;\n"
"	padding: 3px;\n"
"	border-to"
                        "p-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.modifylist_Table_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.modifylist_Table_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.modifylist_Table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.modifylist_Table_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.modifylist_Table_2.setTabKeyNavigation(True)
        self.modifylist_Table_2.setProperty("showDropIndicator", False)
        self.modifylist_Table_2.setDragDropOverwriteMode(False)
        self.modifylist_Table_2.setSortingEnabled(False)
        self.modifylist_Table_2.setWordWrap(False)
        self.modifylist_Table_2.setCornerButtonEnabled(False)
        self.modifylist_Table_2.horizontalHeader().setVisible(False)
        self.modifylist_Table_2.horizontalHeader().setHighlightSections(False)
        self.modifylist_Table_2.verticalHeader().setVisible(False)
        self.modifylist_Table_2.verticalHeader().setHighlightSections(False)

        self.verticalLayout_16.addWidget(self.modifylist_Table_2)

        self.modifylist_Table = QTableView(self.page_modifylist)
        self.modifylist_Table.setObjectName(u"modifylist_Table")
        sizePolicy6.setHeightForWidth(self.modifylist_Table.sizePolicy().hasHeightForWidth())
        self.modifylist_Table.setSizePolicy(sizePolicy6)
        self.modifylist_Table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.modifylist_Table.setTabletTracking(False)
        self.modifylist_Table.setAutoFillBackground(False)
        self.modifylist_Table.setStyleSheet(u"QTableView {	\n"
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
        self.modifylist_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.modifylist_Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.modifylist_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.modifylist_Table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.modifylist_Table.setTabKeyNavigation(True)
        self.modifylist_Table.setProperty("showDropIndicator", False)
        self.modifylist_Table.setDragDropOverwriteMode(False)
        self.modifylist_Table.setSortingEnabled(True)
        self.modifylist_Table.setWordWrap(False)
        self.modifylist_Table.setCornerButtonEnabled(False)
        self.modifylist_Table.verticalHeader().setVisible(False)
        self.modifylist_Table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_16.addWidget(self.modifylist_Table)

        self.frame_13 = QFrame(self.page_modifylist)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy5.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy5)
        self.frame_13.setFont(font2)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.modifylist_addBtn = QPushButton(self.frame_13)
        self.modifylist_addBtn.setObjectName(u"modifylist_addBtn")
        sizePolicy7.setHeightForWidth(self.modifylist_addBtn.sizePolicy().hasHeightForWidth())
        self.modifylist_addBtn.setSizePolicy(sizePolicy7)
        self.modifylist_addBtn.setFont(font)
        self.modifylist_addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifylist_addBtn.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.modifylist_addBtn)

        self.modifylist_removeBtn = QPushButton(self.frame_13)
        self.modifylist_removeBtn.setObjectName(u"modifylist_removeBtn")
        sizePolicy7.setHeightForWidth(self.modifylist_removeBtn.sizePolicy().hasHeightForWidth())
        self.modifylist_removeBtn.setSizePolicy(sizePolicy7)
        self.modifylist_removeBtn.setFont(font)
        self.modifylist_removeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifylist_removeBtn.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.modifylist_removeBtn)

        self.modifylist_finishBtn = QPushButton(self.frame_13)
        self.modifylist_finishBtn.setObjectName(u"modifylist_finishBtn")
        sizePolicy7.setHeightForWidth(self.modifylist_finishBtn.sizePolicy().hasHeightForWidth())
        self.modifylist_finishBtn.setSizePolicy(sizePolicy7)
        self.modifylist_finishBtn.setFont(font)
        self.modifylist_finishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifylist_finishBtn.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.modifylist_finishBtn)


        self.verticalLayout_16.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.page_modifylist)
        self.page_stats = QWidget()
        self.page_stats.setObjectName(u"page_stats")
        self.verticalLayout_7 = QVBoxLayout(self.page_stats)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.statsLabel = QLabel(self.page_stats)
        self.statsLabel.setObjectName(u"statsLabel")
        sizePolicy5.setHeightForWidth(self.statsLabel.sizePolicy().hasHeightForWidth())
        self.statsLabel.setSizePolicy(sizePolicy5)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush19 = QBrush(QColor(210, 210, 210, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush20 = QBrush(QColor(210, 210, 210, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.statsLabel.setPalette(palette2)
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(20)
        font10.setBold(False)
        font10.setWeight(50)
        self.statsLabel.setFont(font10)
        self.statsLabel.setStyleSheet(u"")
        self.statsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.statsLabel)

        self.eodBtn = QPushButton(self.page_stats)
        self.eodBtn.setObjectName(u"eodBtn")
        self.eodBtn.setFont(font)
        self.eodBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eodBtn.setMouseTracking(True)
        self.eodBtn.setLayoutDirection(Qt.LeftToRight)
        self.eodBtn.setAutoFillBackground(False)
        self.eodBtn.setStyleSheet(u"")
        self.eodBtn.setCheckable(False)

        self.verticalLayout_7.addWidget(self.eodBtn)

        self.widget = QWidget(self.page_stats)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.statsTable = QTableView(self.widget)
        self.statsTable.setObjectName(u"statsTable")
        sizePolicy6.setHeightForWidth(self.statsTable.sizePolicy().hasHeightForWidth())
        self.statsTable.setSizePolicy(sizePolicy6)
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

        self.horizontalLayout.addWidget(self.statsTable)


        self.verticalLayout_7.addWidget(self.widget)

        self.revenueBtn = QPushButton(self.page_stats)
        self.revenueBtn.setObjectName(u"revenueBtn")
        self.revenueBtn.setFont(font)
        self.revenueBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.revenueBtn.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.revenueBtn)

        self.revenueLabel = QLabel(self.page_stats)
        self.revenueLabel.setObjectName(u"revenueLabel")
        sizePolicy5.setHeightForWidth(self.revenueLabel.sizePolicy().hasHeightForWidth())
        self.revenueLabel.setSizePolicy(sizePolicy5)
        self.revenueLabel.setFont(font)
        self.revenueLabel.setStyleSheet(u"color: rgb(236, 236, 236);")
        self.revenueLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.revenueLabel)

        self.graphBtn = QPushButton(self.page_stats)
        self.graphBtn.setObjectName(u"graphBtn")
        self.graphBtn.setFont(font)
        self.graphBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.graphBtn.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.graphBtn)

        self.stackedWidget.addWidget(self.page_stats)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.verticalLayout_12 = QVBoxLayout(self.page_help)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.page_help)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_2)

        self.frame_6 = QFrame(self.page_help)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(15)
        self.label_3.setFont(font11)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font11)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_4)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.page_help)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font11)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_5)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font11)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_8)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.page_help)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy9)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy5.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy5)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_9 = QLabel(self.frame_14)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font11)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_9)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font11)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_11)


        self.verticalLayout_17.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_15)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_help)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.verticalLayout_6.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"G8", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MPSS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Group 8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"19CS10020          19CS10034         19CS30046", None))
        self.sell_title_label.setText(QCoreApplication.translate("MainWindow", u"Sell Items", None))
        self.sell_addBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.sell_removeBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.sell_finishBtn.setText(QCoreApplication.translate("MainWindow", u"Finish Order", None))
        self.sell_select_title_label.setText(QCoreApplication.translate("MainWindow", u"Select Items", None))
        self.choiceLabel.setText(QCoreApplication.translate("MainWindow", u"Choose what you want to select from:", None))
        self.sell_select_searchBar.setText("")
        self.sell_select_volLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Volume:", None))
        self.sell_select_volEdit.setText("")
        self.sell_select_priceLabel.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.sell_select_priceEdit.setText("")
        self.sell_select_addBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.sell_select_finishBtn.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.buy_title_label.setText(QCoreApplication.translate("MainWindow", u"Buy Items", None))
        self.buy_addBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.buy_removeBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.buy_orderBtn.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.buy_select_title_label.setText(QCoreApplication.translate("MainWindow", u"Select Items ", None))
        self.choiceLabel_2.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.buy_select_searchBar.setText("")
        self.buy_select_volLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Volume:", None))
        self.buy_select_volEdit.setText("")
        self.buy_select_addBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.buy_select_finishBtn.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.add_remove_title_label.setText(QCoreApplication.translate("MainWindow", u"Modify data", None))
        self.choiceLabel_3.setText(QCoreApplication.translate("MainWindow", u"Select :", None))
        self.add_remove_searchBar.setText("")
        self.add_remove_addBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.add_remove_removeBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.add_remove_modifylistBtn.setText(QCoreApplication.translate("MainWindow", u"Modify List", None))
        self.modifylist_title_label.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.modifylist_addBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.modifylist_removeBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.modifylist_finishBtn.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.statsLabel.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.eodBtn.setText(QCoreApplication.translate("MainWindow", u"End Day", None))
        self.revenueBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Revenue", None))
        self.revenueLabel.setText("")
        self.graphBtn.setText(QCoreApplication.translate("MainWindow", u"Plot Graph", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Developed By:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bhushan Malani", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"bhushanmalani3@gmail.com", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Harshit Jindal", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"jindalharshit0711@gmail.com", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Srijan Das", None))
        self.label_11.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: CIcada 3301", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.3.4", None))
    # retranslateUi

