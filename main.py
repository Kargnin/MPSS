import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *
import databaseOperations
import CustomModel 

from Database import Vendors,Parts,Stats,Invoice,Sales

import matplotlib.pyplot as plt

##GLOBALS
invoice_number_global = databaseOperations.get_globals()[1]
days_passed_global = databaseOperations.get_globals()[0]

## ==> GLOBALS
counter = 0

from UI_SplashScreen import Ui_SplashScreen

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_loading.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_loading.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.label_loading.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 2


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

         ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('MPSS')
        UIFunctions.labelTitle(self, 'MPSS')
        UIFunctions.labelDescription(self, "Day "+str(days_passed_global))
        ## ==> END ##

        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Home", "btn_home", "url(:/icons/icons/home.png)", True)
        UIFunctions.addNewMenu(self, "Sell", "btn_sell", "url(:/icons/icons/sell.png)", True)
        UIFunctions.addNewMenu(self, "Buy", "btn_buy", "url(:/icons/icons/buy.png)", True)
        UIFunctions.addNewMenu(self, "Add/Remove", "btn_add_remove", "url(:/icons/icons/add_remove.png)", True)
        UIFunctions.addNewMenu(self, "Statistics", "btn_stats", "url(:/icons/icons/stats.png)", True)
        UIFunctions.addNewMenu(self, "Help", "btn_help", "url(:/icons/icons/help.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "G8", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        #sell

        self.ui.sell_addBtn.clicked.connect(self.sell_addBtn_clicked)
        self.ui.sell_removeBtn.clicked.connect(self.sell_removeBtn_clicked)
        self.ui.sell_finishBtn.clicked.connect(self.sell_finishBtn_clicked)

        

        self.ui.sell_select_choiceBox.addItems(["Vendor Name","Part Name","Vehicle Type"])

        self.sell_model = CustomModel.CustomTableModelUserData([], ["id_","Invoice No.","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name","Cost Price"],["invoice_number","part_name","vehicle_type","price","volume","amount","vendor_name","cp"],"Invoice")
        self.sell_delegate = CustomModel.InLineEditDelegate()

        self.ui.sell_Table.setModel(self.sell_model)
        self.ui.sell_Table.setItemDelegate(self.sell_delegate)

        self.ui.sell_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.sell_Table.setColumnWidth(0, 30)
        self.ui.sell_Table.hideColumn(0)
        self.ui.sell_Table.hideColumn(8)
        self.ui.sell_Table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.sell_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        #buy

        self.ui.buy_addBtn.clicked.connect(self.buy_addBtn_clicked)
        self.ui.buy_removeBtn.clicked.connect(self.buy_removeBtn_clicked)
        self.ui.buy_orderBtn.clicked.connect(self.buy_finishBtn_clicked)

        self.ui.buy_select_choiceBox.addItems(["Vendor","Part"])

        
        


        self.buy_model = CustomModel.CustomTableModelNoDatabase([], ["id_","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name"],["part_name","vehicle_type","price","volume","amount","vendor_name"],"Invoice")
        self.buy_delegate = CustomModel.InLineEditDelegate()

        self.ui.buy_Table.setModel(self.buy_model)
        self.ui.buy_Table.setItemDelegate(self.buy_delegate)

        self.ui.buy_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.buy_Table.setColumnWidth(0, 30)
        self.ui.buy_Table.hideColumn(0)
        self.ui.buy_Table.hideColumn(8)
        self.ui.buy_Table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.buy_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # #Buy
        # self.ui.buy_addBtn.clicked.connect(self.buy_addBtn_clicked)
        # self.ui.buy_removeBtn.clicked.connect(self.buy_removeBtn_clicked)
        # self.ui.buy_finishBtn.clicked.connect(self.buy_finishBtn_clicked)
        # self.buy_user_data = []
        # self.buy_model = CustomModel.CustomTableModel(self.buy_user_data, ["id_","Invoice No.","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name","Cost Price"],["invoice_number","part_name","vehicle_type","price","volume","amount","vendor_name","cp"],"Invoice")
        # self.buy_delegate = CustomModel.InLineEditDelegate()

        # self.ui.buy_Table.setModel(self.buy_model)
        # self.ui.buy_Table.setItemDelegate(self.buy_delegate)

        # self.ui.buy_Table.verticalHeader().setDefaultSectionSize(50)
        # self.ui.buy_Table.setColumnWidth(0, 30)
        # self.ui.buy_Table.hideColumn(0)
        # self.ui.buy_Table.hideColumn(1)
        # self.ui.buy_Table.setSelectionBehavior(QTableView.SelectRows)
        # self.ui.buy_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        ## ==> PAGE ADD/REMOVE 
        ########################################################################

        ## ==> ADD_REMOVE_TABLE PARAMETERS
        ########################################################################
        #Set ComboBox
        self.ui.add_remove_choiceBox.addItems(["Vendors","Parts"])
        self.ui.add_remove_choiceBox.currentIndexChanged.connect(self.add_remove_choiceBox_selectionchanged)

        #Show Vendors Data Initially
        self.add_remove_model = CustomModel.CustomTableModel(Vendors())
        self.add_remove_delegate = CustomModel.InLineEditDelegate()
        
        #Filter model
        self.add_remove_filter_proxy_model = QtCore.QSortFilterProxyModel()
        self.add_remove_filter_proxy_model.setSourceModel(self.add_remove_model)
        self.add_remove_filter_proxy_model.setFilterKeyColumn(1)
        
        #SearchBar
        self.add_remove_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.ui.add_remove_searchBar.textChanged.connect(self.add_remove_filter_proxy_model.setFilterRegExp)

        #Initial Table
        self.ui.add_remove_Table.setModel(self.add_remove_filter_proxy_model)
        self.ui.add_remove_Table.setItemDelegate(self.add_remove_delegate)
        self.ui.add_remove_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.add_remove_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.add_remove_Table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.ui.add_remove_Table.hideColumn(0)

        
        self.ui.add_remove_addBtn.clicked.connect(self.add_remove_addBtn_clicked)
        self.ui.add_remove_removeBtn.clicked.connect(self.add_remove_removeBtn_clicked)
        self.ui.add_remove_modifylistBtn.clicked.connect(self.add_remove_modifylist_clicked)

        self.ui.modifylist_addBtn.clicked.connect(self.modifylist_addBtn_clicked)
        self.ui.modifylist_removeBtn.clicked.connect(self.modifylist_removeBtn_clicked)
        self.ui.modifylist_finishBtn.clicked.connect(self.modifylist_finishBtn_clicked)

        ## ==> END ##    

        ## ==> END ## 

        ## ==> PAGE STATS 
        ########################################################################



        ## ==> STATSTABLE PARAMETERS
        ########################################################################
        
        
        self.stats_model = CustomModel.CustomTableModelThreshold(Stats())
        # self.delegate = CustomModel.InLineEditDelegate()
        self.ui.statsTable.setModel(self.stats_model)
        self.ui.statsTable.verticalHeader().setDefaultSectionSize(50)
        self.ui.statsTable.setColumnWidth(0, 30)
        self.ui.statsTable.hideColumn(0)
        self.ui.statsTable.hideColumn(5)

        self.ui.statsTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)



        self.ui.eodBtn.clicked.connect(self.eodBtn_clicked)
        self.ui.revenueBtn.clicked.connect(self.generate_revenue)
        self.ui.graphBtn.clicked.connect(self.show_plot)


        ## ==> END ##    

        ## ==> END ##    
        

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

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


    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE SELL
        if btnWidget.objectName() == "btn_sell":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_sell)
            UIFunctions.resetStyle(self, "btn_sell")
            UIFunctions.labelPage(self, "Sell")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE BUY
        if btnWidget.objectName() == "btn_buy":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_buy)
            UIFunctions.resetStyle(self, "btn_buy")
            UIFunctions.labelPage(self, "Buy")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE ADD/REMOVE
        if btnWidget.objectName() == "btn_add_remove":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_remove)
            UIFunctions.resetStyle(self, "btn_add_remove")
            UIFunctions.labelPage(self, "Add/remove")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE STATS
        if btnWidget.objectName() == "btn_stats":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_stats)
            UIFunctions.resetStyle(self, "btn_stats")
            UIFunctions.labelPage(self, "Statistics")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            
            self.stats_model = CustomModel.CustomTableModelThreshold(Stats())
            # self.delegate = CustomModel.InLineEditDelegate()
            self.ui.statsTable.setModel(self.stats_model)
            self.ui.statsTable.verticalHeader().setDefaultSectionSize(50)
            self.ui.statsTable.setColumnWidth(0, 30)
            self.ui.statsTable.hideColumn(0)
            self.ui.statsTable.hideColumn(5)

            self.ui.statsTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # PAGE STATS
        if btnWidget.objectName() == "btn_help":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_help)
            UIFunctions.resetStyle(self, "btn_help")
            UIFunctions.labelPage(self, "Help")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##


    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print()
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    # def keyPressEvent(self, event):
    #     print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    #SELL
    def selectionchange_sell_select(self,i):
        self.sell_select_filter_proxy_model.setFilterKeyColumn(i+1)

    def sell_addBtn_clicked(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sell_select)
        self.ui.sell_select_finishBtn.clicked.connect(self.sell_select_finishBtn_clicked)
        self.ui.sell_select_addBtn.clicked.connect(self.sell_select_addBtn_clicked)
        
        self.ui.sell_select_volEdit.setText("1")
        

        self.sell_select_model = CustomModel.CustomTableModel(Stats())
        self.sell_select_delegate = CustomModel.InLineEditDelegate()
        self.sell_select_filter_proxy_model = QtCore.QSortFilterProxyModel()
        self.sell_select_filter_proxy_model.setSourceModel(self.sell_select_model)

        self.sell_select_filter_proxy_model.setFilterKeyColumn(self.ui.sell_select_choiceBox.currentIndex()+1)
        self.ui.sell_select_choiceBox.currentIndexChanged.connect(self.selectionchange_sell_select)
        
        self.sell_select_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.ui.sell_select_searchBar.textChanged.connect(self.sell_select_filter_proxy_model.setFilterRegExp)

        self.ui.sell_select_Table.setModel(self.sell_select_filter_proxy_model)
        self.ui.sell_select_Table.setItemDelegate(self.sell_select_delegate)
        self.ui.sell_select_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.sell_select_Table.setColumnWidth(0, 30)
        self.ui.sell_select_Table.hideColumn(0)
        self.ui.sell_Table.hideColumn(8)
        self.ui.sell_select_Table.setSelectionBehavior(QTableView.SelectRows)
        

        self.ui.sell_select_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def sell_select_finishBtn_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sell)

    def sell_removeBtn_clicked(self):

        if self.ui.sell_Table.selectionModel().selectedRows() == None:
            return

        vol = self.ui.sell_Table.selectedIndexes()[4].data()
        vendor = self.ui.sell_Table.selectedIndexes()[6].data()
        part = self.ui.sell_Table.selectedIndexes()[1].data()
        vehicle = self.ui.sell_Table.selectedIndexes()[2].data()
        self.sell_model.removeRows(invoice_number_global,self.ui.sell_Table.selectedIndexes()[0])
        databaseOperations.update_existing_stock_add(vol,vendor,part,vehicle)
        self.sell_addBtn_clicked()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sell)


    def sell_select_addBtn_clicked(self):
        if self.ui.sell_select_Table.selectionModel().selectedRows() == None:
            return

        
        data = []
        data.append(invoice_number_global)
        # for i in range (5):
        #     print(self.ui.sell_select_Table.selectedIndexes()[i].data())

        data.append(self.ui.sell_select_Table.selectedIndexes()[1].data())
        data.append(self.ui.sell_select_Table.selectedIndexes()[2].data())
        if self.ui.sell_select_priceEdit.text() != "" :
            if float(self.ui.sell_select_priceEdit.text()) >= 0: 
                data.append(float(self.ui.sell_select_priceEdit.text()))
            else:
                data.append(-1*float(self.ui.sell_select_priceEdit.text()))
                self.ui.sell_select_priceEdit.setText(str(-1*float(self.ui.sell_select_priceEdit.text())))
        else:
            self.ui.sell_select_priceEdit.setText("0")
            data.append(0)

        if int(self.ui.sell_select_volEdit.text()) <= self.ui.sell_select_Table.selectedIndexes()[3].data():
            data.append(int(self.ui.sell_select_volEdit.text()))

        else:
            self.ui.sell_select_volEdit.setText(str(self.ui.sell_select_Table.selectedIndexes()[3].data()))
            data.append(self.ui.sell_select_Table.selectedIndexes()[3].data())

        data.append(float(self.ui.sell_select_priceEdit.text()) * int(self.ui.sell_select_volEdit.text()))
        data.append(self.ui.sell_select_Table.selectedIndexes()[0].data())
        data.append(self.ui.sell_select_Table.selectedIndexes()[4].data())

        databaseOperations.insert_data(data,["invoice_number","part_name","vehicle_type","price","volume","amount","vendor_name","cp"],"Invoice")

        self.sell_model = CustomModel.CustomTableModelUserData(databaseOperations.get_multiple_data_invoice(invoice_number_global,"Invoice"), ["id_","Invoice No.","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name","Cost Price"],["invoice_number","part_name","vehicle_type","price","volume","amount","vendor_name","cp"],"Invoice")

        self.ui.sell_Table.setModel(self.sell_model)

        self.ui.sell_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.sell_Table.setColumnWidth(0, 30)
        self.ui.sell_Table.hideColumn(0)
        self.ui.sell_Table.hideColumn(8)
        self.ui.sell_Table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.sell_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        databaseOperations.update_existing_stock(data[4],data[6],data[1],data[2])

        self.sell_addBtn_clicked()


    def sell_finishBtn_clicked(self):
        if self.sell_model.rowCount() == 0:
            return
        for row in range(self.sell_model.rowCount()):
            role = Qt.DisplayRole
            vol = self.sell_model.data(self.sell_model.index(row,5),role)
            vendor = self.sell_model.data(self.sell_model.index(row,7),role)
            part = self.sell_model.data(self.sell_model.index(row,2),role)
            vehicle = self.sell_model.data(self.sell_model.index(row,3),role)

            # databaseOperations.update_existing_stock(vol,vendor,part,vehicle)
            databaseOperations.update_existing_Threshold(days_passed_global,vol,part,vehicle)

        self.sell_model = CustomModel.CustomTableModelUserData([], ["id_","Invoice No.","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name","Cost Price"],["invoice_number","part_name","vehicle_type","price","volume","amount","vendor_name","cp"],"Invoice")
        self.sell_delegate = CustomModel.InLineEditDelegate()

        self.ui.sell_Table.setModel(self.sell_model)
        self.ui.sell_Table.setItemDelegate(self.sell_delegate)

        self.ui.sell_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.sell_Table.setColumnWidth(0, 30)
        self.ui.sell_Table.hideColumn(0)
        self.ui.sell_Table.hideColumn(8)
        self.ui.sell_Table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.sell_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        databaseOperations.insert_data([days_passed_global,invoice_number_global],["Date","invoice_number"],"Sales")

        update_invoice_number()
        
    ## ==> END ##

    #BUY
    def selectionchange_buy_select(self,i):
        if i == 0:
            self.buy_select_filter_proxy_model.setFilterKeyColumn(6)
        else:
            self.buy_select_filter_proxy_model.setFilterKeyColumn(1)

    def buy_addBtn_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_buy_select)
        self.ui.buy_select_finishBtn.clicked.connect(self.buy_select_finishBtn_clicked)
        self.ui.buy_select_addBtn.clicked.connect(self.buy_select_addBtn_clicked)
        self.ui.buy_select_volEdit.setText("1")
        

        self.buy_select_model = CustomModel.CustomTableModel(Stats())
        self.buy_select_delegate = CustomModel.InLineEditDelegate()
        self.buy_select_filter_proxy_model = QtCore.QSortFilterProxyModel()
        self.buy_select_filter_proxy_model.setSourceModel(self.buy_select_model)

        if self.ui.buy_select_choiceBox.currentIndex() == 0:
            self.buy_select_filter_proxy_model.setFilterKeyColumn(6)
        else:
            self.buy_select_filter_proxy_model.setFilterKeyColumn(1)
        
        self.ui.buy_select_choiceBox.currentIndexChanged.connect(self.selectionchange_buy_select)
        
        self.buy_select_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.ui.buy_select_searchBar.textChanged.connect(self.buy_select_filter_proxy_model.setFilterRegExp)

        self.ui.buy_select_Table.setModel(self.buy_select_filter_proxy_model)
        self.ui.buy_select_Table.setItemDelegate(self.buy_select_delegate)
        self.ui.buy_select_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.buy_select_Table.setColumnWidth(0, 30)
        self.ui.buy_select_Table.hideColumn(0)
        self.ui.buy_Table.hideColumn(8)
        self.ui.buy_select_Table.setSelectionBehavior(QTableView.SelectRows)
        

        self.ui.buy_select_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def buy_select_finishBtn_clicked(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_buy)
        
        self.buy_model = CustomModel.CustomTableModelNoDatabase(self.buy_model.user_data, ["id_","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name"],["part_name","vehicle_type","price","volume","amount","vendor_name"],"Invoice")
        self.buy_delegate = CustomModel.InLineEditDelegate()
        self.ui.buy_Table.setModel(self.buy_model)

        self.ui.buy_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.buy_Table.setColumnWidth(0, 30)
        self.ui.buy_Table.hideColumn(0)
        self.ui.buy_Table.hideColumn(8)
        self.ui.buy_Table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.buy_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def buy_removeBtn_clicked(self):

        if self.ui.buy_Table.selectionModel().selectedRows() == None:
            return

        vol = self.ui.buy_Table.selectedIndexes()[3].data()
        vendor = self.ui.buy_Table.selectedIndexes()[5].data()
        part = self.ui.buy_Table.selectedIndexes()[0].data()
        vehicle = self.ui.buy_Table.selectedIndexes()[1].data()
        self.buy_model.removeRows(invoice_number_global,self.ui.buy_Table.selectedIndexes()[0])
        databaseOperations.update_existing_stock_add(vol,vendor,part,vehicle)
        self.buy_addBtn_clicked()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_buy)


    def buy_select_addBtn_clicked(self):
        if self.ui.buy_select_Table.selectionModel().selectedRows() == None:
            return

        
        data = []
        
        # for i in range (5):
        #     print(self.ui.buy_select_Table.selectedIndexes()[i].data())

        data.append(self.ui.buy_select_Table.selectedIndexes()[1].data())
        data.append(self.ui.buy_select_Table.selectedIndexes()[2].data())
        
        data.append(float(self.ui.buy_select_Table.selectedIndexes()[4].data()))

        if int(self.ui.buy_select_volEdit.text()) <= self.ui.buy_select_Table.selectedIndexes()[3].data():
            data.append(int(self.ui.buy_select_volEdit.text()))

        else:
            self.ui.buy_select_volEdit.setText(str(self.ui.buy_select_Table.selectedIndexes()[3].data()))
            data.append(self.ui.buy_select_Table.selectedIndexes()[3].data())

        data.append(float(self.ui.buy_select_Table.selectedIndexes()[4].data()) * int(self.ui.buy_select_volEdit.text()))
        data.append(self.ui.buy_select_Table.selectedIndexes()[0].data())
        data.append(self.ui.buy_select_Table.selectedIndexes()[4].data())


        new_data = [len(self.buy_model.user_data)]
        
        self.buy_model.add_data(tuple(new_data + data))

        self.ui.buy_Table.setModel(self.buy_model)

        self.ui.buy_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.buy_Table.setColumnWidth(0, 30)
        self.ui.buy_Table.hideColumn(0)
        self.ui.buy_Table.hideColumn(8)
        self.ui.buy_Table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.buy_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)



        self.buy_addBtn_clicked()


    def buy_finishBtn_clicked(self):
        if self.buy_model.rowCount() == 0:
            return
        for row in range(self.buy_model.rowCount()):
            role = Qt.DisplayRole
            vol = self.buy_model.data(self.buy_model.index(row,5),role)
            vendor = self.buy_model.data(self.buy_model.index(row,7),role)
            part = self.buy_model.data(self.buy_model.index(row,2),role)
            vehicle = self.buy_model.data(self.buy_model.index(row,3),role)

            # databaseOperations.update_existing_stock(vol,vendor,part,vehicle)
            # databaseOperations.update_existing_Threshold(days_passed_global,vol,part,vehicle)

        self.buy_model = CustomModel.CustomTableModelUserData([], ["id_","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name"],["part_name","vehicle_type","price","volume","amount","vendor_name"],"Invoice")
        self.buy_delegate = CustomModel.InLineEditDelegate()

        self.ui.buy_Table.setModel(self.buy_model)
        self.ui.buy_Table.setItemDelegate(self.buy_delegate)

        self.ui.buy_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.buy_Table.setColumnWidth(0, 30)
        self.ui.buy_Table.hideColumn(0)
        self.ui.buy_Table.hideColumn(8)
        self.ui.buy_Table.setSelectionBehavior(QTableView.SelectRows)
        self.ui.buy_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        
    ## ==> END ##




    ## ADD/REMOVE PAGE
    def add_remove_choiceBox_selectionchanged(self,index):
        if(index == 0):
            self.add_remove_model = CustomModel.CustomTableModel(Vendors())
            self.add_remove_delegate = CustomModel.InLineEditDelegate()

            self.add_remove_filter_proxy_model = QtCore.QSortFilterProxyModel()
            self.add_remove_filter_proxy_model.setSourceModel(self.add_remove_model)
            self.add_remove_filter_proxy_model.setFilterKeyColumn(1)

            self.add_remove_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
            self.ui.add_remove_searchBar.textChanged.connect(self.add_remove_filter_proxy_model.setFilterRegExp)

            self.ui.add_remove_Table.setModel(self.add_remove_filter_proxy_model)
            self.ui.add_remove_Table.setItemDelegate(self.add_remove_delegate)
            
            self.ui.add_remove_Table.hideColumn(0)
        else:
            self.add_remove_model = CustomModel.CustomTableModel(Parts())
            self.add_remove_delegate = CustomModel.InLineEditDelegate()

            self.add_remove_filter_proxy_model = QtCore.QSortFilterProxyModel()
            self.add_remove_filter_proxy_model.setSourceModel(self.add_remove_model)
            self.add_remove_filter_proxy_model.setFilterKeyColumn(1)

            self.add_remove_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
            self.ui.add_remove_searchBar.textChanged.connect(self.add_remove_filter_proxy_model.setFilterRegExp)


            self.ui.add_remove_Table.setModel(self.add_remove_filter_proxy_model)
            self.ui.add_remove_Table.setItemDelegate(self.add_remove_delegate)

            self.ui.add_remove_Table.hideColumn(0)
            self.ui.add_remove_Table.hideColumn(4)

        self.ui.add_remove_Table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.add_remove_Table.verticalHeader().setDefaultSectionSize(50)
        self.ui.add_remove_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def add_remove_addBtn_clicked(self,clicked):
        self.add_remove_model.insertRows() 

    def add_remove_modifyBtn_clicked(self,clicked):
        pass

    def add_remove_removeBtn_clicked(self,clicked):

        if len(self.ui.add_remove_Table.selectedIndexes()) == 0:
            print("None selected")
            return

        # print(len(self.ui.add_remove_Table.selectedIndexes()))

        # print(self.ui.add_remove_Table.selectedIndexes()[0].data())
        if self.ui.add_remove_choiceBox.currentIndex() == 0:
            
            self.add_remove_model.removeRows_vendor_part([self.ui.add_remove_Table.selectedIndexes()[0].data()])
        else:
            self.add_remove_model.removeRows_vendor_part([self.ui.add_remove_Table.selectedIndexes()[0].data(),self.ui.add_remove_Table.selectedIndexes()[1].data()])


    def add_remove_modifylist_clicked(self,clicked):

        if len(self.ui.add_remove_Table.selectedIndexes()) == 0:
            print("None selected")
            return

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_modifylist)

        if self.ui.add_remove_choiceBox.currentIndex() == 0:
            self.ui.modifylist_title_label.setText("List of Parts Sold")
            

        else:
            self.ui.modifylist_title_label.setText("List of Vendors Selling")

        
        rowid = self.ui.add_remove_Table.selectedIndexes()[0].row()

        l = [self.add_remove_model.user_data[rowid]]
        self.ui.modifylist_Table_2.setModel(CustomModel.CustomTableModelNoHeaders(l,["id_","Name",".","."]))
        self.ui.modifylist_Table_2.setItemDelegate(self.add_remove_delegate)
        self.ui.modifylist_Table_2.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.modifylist_Table_2.verticalHeader().setDefaultSectionSize(50)
        self.ui.modifylist_Table_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.modifylist_Table_2.hideColumn(0)


        self.modifylist_model = CustomModel.CustomTableModel(Stats())
        self.modifylist_delegate = CustomModel.InLineEditDelegate()

        self.modifylist_filter_proxy_model = QtCore.QSortFilterProxyModel()
        self.modifylist_filter_proxy_model.setSourceModel(self.modifylist_model)

        if self.ui.add_remove_choiceBox.currentIndex() == 0:

            self.modifylist_filter_proxy_model.setFilterKeyColumn(1)

            # self.add_remove_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

            #Filter Data
            self.modifylist_filter_proxy_model.setFilterRegExp(str(l[0][1]))

            self.ui.modifylist_Table.setModel(self.modifylist_filter_proxy_model)
            self.ui.modifylist_Table.setItemDelegate(self.modifylist_delegate)
            self.ui.modifylist_Table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.ui.modifylist_Table.verticalHeader().setDefaultSectionSize(50)
            self.ui.modifylist_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.ui.modifylist_Table.hideColumn(0)
            self.ui.modifylist_Table.hideColumn(1)
            self.ui.modifylist_Table.showColumn(2)
            self.ui.modifylist_Table.showColumn(3)
            self.ui.modifylist_Table.hideColumn(4)

        else:

            self.modifylist_filter_proxy_model.setFilterKeyColumn(2)

            # self.add_remove_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

            #Filter Data
            self.modifylist_filter_proxy_model.setFilterRegExp(str(l[0][1]))

            self.modifylist_filter_proxy_model_1 = QtCore.QSortFilterProxyModel()
            self.modifylist_filter_proxy_model_1.setSourceModel(self.modifylist_filter_proxy_model)
            self.modifylist_filter_proxy_model_1.setFilterKeyColumn(3)
            self.modifylist_filter_proxy_model_1.setFilterRegExp(str(l[0][2]))

            self.ui.modifylist_Table.setModel(self.modifylist_filter_proxy_model_1)
            self.ui.modifylist_Table.setItemDelegate(self.modifylist_delegate)
            self.ui.modifylist_Table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            self.ui.modifylist_Table.verticalHeader().setDefaultSectionSize(50)
            self.ui.modifylist_Table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.ui.modifylist_Table.hideColumn(0)
            if self.ui.modifylist_Table.isColumnHidden(1):
                self.ui.modifylist_Table.showColumn(1)
            self.ui.modifylist_Table.hideColumn(2)
            self.ui.modifylist_Table.hideColumn(3)
            self.ui.modifylist_Table.hideColumn(4)

    def modifylist_addBtn_clicked(self,clicked):
        
        if self.ui.add_remove_choiceBox.currentIndex() == 0:
            rowid = self.ui.add_remove_Table.selectedIndexes()[0].row()
            l = [self.add_remove_model.user_data[rowid]]
            
            self.modifylist_model.insertRows_vendor_part([str(l[0][1])])
            self.add_remove_modifylist_clicked(0)
        else:
            rowid = self.ui.add_remove_Table.selectedIndexes()[0].row()
            l = [self.add_remove_model.user_data[rowid]]
            print(l)
            self.modifylist_model.insertRows_vendor_part([str(l[0][1]),str(l[0][2])])
            self.add_remove_modifylist_clicked(1)
    def modifylist_modifyBtn_clicked(self,clicked):
        pass

    def modifylist_removeBtn_clicked(self,clicked):

        if len(self.ui.modifylist_Table.selectedIndexes()) == 0:
            print("None selected")
            return
        if self.ui.add_remove_choiceBox.currentIndex() == 0:
            rowid = self.ui.add_remove_Table.selectedIndexes()[0].row()
            l = [self.add_remove_model.user_data[rowid]]
            
            self.modifylist_model.removeRows_fromList([str(l[0][1])],[self.ui.modifylist_Table.selectedIndexes()[0].data(),self.ui.modifylist_Table.selectedIndexes()[1].data()])
            self.add_remove_modifylist_clicked(0)
        else:
            rowid = self.ui.add_remove_Table.selectedIndexes()[0].row()
            l = [self.add_remove_model.user_data[rowid]]
            self.modifylist_model.removeRows_fromList([str(l[0][1]),str(l[0][2])],[self.ui.modifylist_Table.selectedIndexes()[0].data()])
            self.add_remove_modifylist_clicked(1)

    def modifylist_finishBtn_clicked(self,clicked):

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_remove)

    def eodBtn_clicked(self,clicked):
        global days_passed_global
        days_passed_global+=1
        databaseOperations.update_globals([days_passed_global,invoice_number_global])
        UIFunctions.labelDescription(self, "Day "+str(days_passed_global))

    def generate_revenue(self,clicked):
        sales_data = databaseOperations.get_multiple_data_days(days_passed_global,"Sales")

        invoice_number= []
        for data in sales_data:
            invoice_number.append(data[2])

        sum_ = 0.0

        for invoices in invoice_number:
            for d in databaseOperations.get_multiple_data_invoice(invoices,"Invoice"):
                print(d)
                sum_ += (d[4] - d[8]) * d[5]
                print(sum_)




        self.ui.revenueLabel.setText("Revenue generated = Rs. {:.2f}".format(sum_) )

    def show_plot(self,clicked):
        
        global days_passed_global
        x = []
        y = []

        if days_passed_global > 30:
            k = days_passed_global - 30
        else:
            k = 1

        for i in range(k,days_passed_global+1):
            x.append(i)
            sales_data = databaseOperations.get_multiple_data_days(i,"Sales")

            invoice_number= []
            for data in sales_data:
                invoice_number.append(data[2])

            vol = 0

            for invoices in invoice_number:
                for d in databaseOperations.get_multiple_data_invoice(invoices,"Invoice"):
                    vol += d[5]

            y.append(vol)


        
        plt.xlabel('Day')
        plt.ylabel('Total Vol. Sold')
        plt.plot(x,y,'ro')
        plt.show()

def update_invoice_number():
    global invoice_number_global
    global days_passed_global
    invoice_number_global += 1
    databaseOperations.update_globals([days_passed_global,invoice_number_global])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')

    
    window = SplashScreen()
    sys.exit(app.exec_())
