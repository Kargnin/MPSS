import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Shapes 1.15
import QtGraphicalEffects 1.15
import "controls"
import QtQuick.Controls 2.15
Window {
    id: mainWindow
    width: 1000
    height: 580
    minimumWidth: 800
    minimumHeight: 500
    visible: true
    color: "#00000000"

    //Removing TitleBar
    flags: Qt.Window | Qt.FramelessWindowHint

    //Properties
    property int windowStatus: 0
    property int appborder: 5

    //Internal Functions
    QtObject{
        id: internal
        function maximizeRestore(){
            if(windowStatus == 0){
                windowStatus = 1
                appborder = 0
                resizeBottom.visible = false
                resizeLeft.visible = false
                resizeRight.visible = false
                resizeTop.visible = false
                resizeBottomLeft.visible = false
                resizeBottomRight.visible = false
                resizeTopLeft.visible = false
                resizeTopRight.visible = false
                mainWindow.showMaximized()

            }
            else{
                windowStatus = 0
                appborder = 5
                resizeBottom.visible = true
                resizeLeft.visible = true
                resizeRight.visible = true
                resizeTop.visible = true
                resizeBottomLeft.visible = true
                resizeBottomRight.visible = true
                resizeTopLeft.visible = true
                resizeTopRight.visible = true
                mainWindow.showNormal()
            }
        }

    }

    title: qsTr("MPSS")


    Rectangle {
        id: mouseAreaContainer
        color: "#00000000"
        anchors.fill: parent

        Rectangle {
            id: bg
            x: 5
            y: 5
            opacity: 1
            visible: true
            color: "#00000000"
            radius: 10
            anchors.fill: parent
            anchors.rightMargin: appborder
            anchors.leftMargin: appborder
            anchors.bottomMargin: appborder
            anchors.topMargin: appborder

            Rectangle {
                id: appContainer
                visible: true
                color: "#222831"
                radius: 10
                border.color: "#222831"
                anchors.fill: parent
                z: 1

                Rectangle {
                    id: topBarContainer
                    height: 55
                    color: "#1b2129"
                    radius: 10
                    border.color: "#1b2129"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.rightMargin: 0
                    anchors.leftMargin: 2
                    anchors.topMargin: 0

                    //            Button {
                    //                id: toggleButton
                    //                width: 55
                    //                text: qsTr("Button")
                    //                anchors.left: parent.left
                    //                anchors.top: parent.top
                    //                anchors.bottom: parent.bottom
                    //                flat: false
                    //                anchors.leftMargin: 0
                    //                anchors.bottomMargin: 0
                    //                anchors.topMargin: 0
                    //            }

                    ToggleButton{
                        anchors.left: parent.left
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        anchors.leftMargin: 0
                        onClicked: animationMenu.running = true

                    }

                    Rectangle {
                        id: topBarTopContainer
                        height: 40
                        //                height: 40
                        visible: true
                        color: "#1b2129"
                        radius: 10
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.rightMargin: 0
                        anchors.leftMargin: 55
                        anchors.topMargin: 0

                        //Drag Option
                        DragHandler{
                            onActiveChanged: if(active){
                                                 mainWindow.startSystemMove()
                                             }
                        }

                        Row {
                            id: windowOptions
                            x: 771
                            width: 135
                            height: 40
                            anchors.right: parent.right
                            anchors.top: parent.top
                            anchors.bottom: parent.bottom
                            anchors.rightMargin: 2
                            spacing: 5
                            layoutDirection: Qt.LeftToRight

                            //                    Button {
                            //                        id: minimise
                            //                        width: 50
                            //                        text: qsTr("minimise")
                            //                        anchors.left: parent.left
                            //                        anchors.top: parent.top
                            //                        anchors.bottom: parent.bottom
                            //                        wheelEnabled: false
                            //                        spacing: 0
                            //                        focusPolicy: Qt.StrongFocus
                            //                    }
                            Minimise{
                                id: minimise
                                visible: true
                                focusPolicy: Qt.ClickFocus
                                onClicked: mainWindow.showMinimized()

                            }

                            Minimise {
                                id: maximise
                                focusPolicy: Qt.ClickFocus
                                btnIconSource: "../images/svg_images/maximize_white_24dp.svg"
                                onClicked: internal.maximizeRestore()
                            }

                            Minimise {
                                id: close
                                btnColorMouseOver: "#e84545"
                                focusPolicy: Qt.ClickFocus
                                btnIconSource: "../images/svg_images/close_white_24dp.svg"
                                onClicked: mainWindow.close()
                            }

                            //                    Button {
                            //                        id: maximise
                            //                        width: 50
                            //                        text: qsTr("maximise")
                            //                        anchors.left: minimise.right
                            //                        anchors.top: parent.top
                            //                        anchors.bottom: parent.bottom
                            //                        anchors.leftMargin: 0
                            //                    }

                            //                    Button {
                            //                        id: close
                            //                        text: qsTr("close")
                            //                        anchors.left: maximise.right
                            //                        anchors.right: parent.right
                            //                        anchors.top: parent.top
                            //                        anchors.bottom: parent.bottom
                            //                        padding: 0
                            //                        anchors.leftMargin: 0
                            //                        anchors.rightMargin: 0
                            //                    }
                        }

                        Text {
                            id: text1
                            y: 13
                            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ececec;\">MPSS</span></p></body></html>"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: parent.left
                            font.pixelSize: 12
                            anchors.verticalCenterOffset: 0
                            anchors.leftMargin: 10
                            textFormat: Text.RichText
                        }
                    }

                    Rectangle {
                        id: topBarBottomContainer
                        color: "#282f3a"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.bottomMargin: 0
                        anchors.rightMargin: 0
                        anchors.topMargin: 40
                        anchors.leftMargin: 55

                        Label {
                            id: appDescription
                            color: "#ececec"
                            text: qsTr("Motor Part Shop System")
                            anchors.fill: parent
                            leftInset: 0
                            leftPadding: 10
                            rightInset: 0
                            rightPadding: 0
                            font.family: "Seogue Ui"
                            styleColor: "#ececec"
                            anchors.rightMargin: 250
                        }

                        Label {
                            id: appDescription_creator
                            color: "#ececec"
                            text: qsTr("Group 8")
                            anchors.left: appDescription.right
                            anchors.right: parent.right
                            anchors.top: parent.top
                            anchors.bottom: parent.bottom
                            horizontalAlignment: Text.AlignRight
                            anchors.leftMargin: 0
                            leftInset: 0
                            styleColor: "#ececec"
                            leftPadding: 0
                            font.family: "Seogue Ui"
                            rightInset: 0
                            rightPadding: 10
                        }
                    }
                }

                Rectangle {
                    id: content
                    x: 2
                    y: 0
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: topBarContainer.bottom
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 0

                    Rectangle {
                        id: pageContainer
                        color: "#00000000"
                        radius: 10
                        anchors.left: toggleBarContainer.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.leftMargin: 0
                        anchors.topMargin: 0

                        //                        StackView {
                        //                            id: stackView
                        //                            anchors.fill: parent
                        //                        }

                        Loader {
                            id:pageHome
                            anchors.fill: parent
                            source:Qt.resolvedUrl("pages/homePage.qml")
                            visible: true
                        }

                        Loader {
                            id:pageSell
                            anchors.fill: parent
                            source:Qt.resolvedUrl("pages/sellPage.qml")
                            visible: false
                        }

                        Loader {
                            id:pageBuy
                            anchors.fill: parent
                            source:Qt.resolvedUrl("pages/buyPage.qml")
                            visible: false
                        }

                        Loader {
                            id:pageAddRemove
                            anchors.fill: parent
                            source:Qt.resolvedUrl("pages/add_removePage.qml")
                            visible: false
                        }

                        Loader {
                            id:pageStats
                            anchors.fill: parent
                            source:Qt.resolvedUrl("pages/statsPage.qml")
                            visible: false
                        }

                        Loader {
                            id:pageHelp
                            anchors.fill: parent
                            source:Qt.resolvedUrl("pages/helpPage.qml")
                            visible: false
                        }
                    }

                    Rectangle {
                        id: toggleBarContainer
                        x: 1
                        y: 0
                        width: 55
                        color: "#1b2129"
                        radius: 10
                        border.color: "#1b2129"
                        anchors.left: parent.left
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        clip: true
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0

                        PropertyAnimation{
                            id:animationMenu
                            target: toggleBarContainer
                            property: "width"
                            to: if(toggleBarContainer.width == 55) return 160;else return 55
                            duration: 600
                            easing.type: Easing.InOutQuint
                        }

                        Column {
                            id: togglecolumn
                            anchors.left: parent.left
                            anchors.right: parent.right
                            anchors.top: parent.top
                            anchors.bottom: parent.bottom
                            anchors.rightMargin: 0
                            anchors.leftMargin: 0
                            anchors.bottomMargin: 100
                            anchors.topMargin: 0
                            bottomPadding: 10
                            padding: 0
                            spacing: 0

                            LeftMenuBtn{
                                id:btnHome
                                width: toggleBarContainer.width
                                text: qsTr("Home")
                                isActiveMenu: true
                                btnIconSource: "../images/svg_images/home_white_24dp.svg"
                                onClicked: {
                                    btnHome.isActiveMenu = true
                                    btnSell.isActiveMenu = false
                                    btnBuy.isActiveMenu = false
                                    btnAddRemove.isActiveMenu = false
                                    btnStats.isActiveMenu = false
                                    btnHelp.isActiveMenu = false
                                    pageHome.visible = true
                                    pageSell.visible = false
                                    pageBuy.visible = false
                                    pageAddRemove.visible = false
                                    pageStats.visible = false
                                    pageHelp.visible = false
                                }
                            }

                            LeftMenuBtn {
                                id: btnSell
                                width: toggleBarContainer.width
                                text: qsTr("Sell")
                                btnIconSource: "../images/svg_images/sell_white_24dp.svg"
                                onClicked: {
                                    btnHome.isActiveMenu = false
                                    btnSell.isActiveMenu = true
                                    btnBuy.isActiveMenu = false
                                    btnAddRemove.isActiveMenu = false
                                    btnStats.isActiveMenu = false
                                    btnHelp.isActiveMenu = false
                                    pageHome.visible = false
                                    pageSell.visible = true
                                    pageBuy.visible = false
                                    pageAddRemove.visible = false
                                    pageStats.visible = false
                                    pageHelp.visible = false
                                }
                            }

                            LeftMenuBtn {
                                id: btnBuy
                                width: toggleBarContainer.width
                                text: qsTr("Buy")
                                btnIconSource: "../images/svg_images/shopping_cart_white_24dp.svg"
                                onClicked: {
                                    btnHome.isActiveMenu = false
                                    btnSell.isActiveMenu = false
                                    btnBuy.isActiveMenu = true
                                    btnAddRemove.isActiveMenu = false
                                    btnStats.isActiveMenu = false
                                    btnHelp.isActiveMenu = false
                                    pageHome.visible = false
                                    pageSell.visible = false
                                    pageBuy.visible = true
                                    pageAddRemove.visible = false
                                    pageStats.visible = false
                                    pageHelp.visible = false
                                }
                            }

                            LeftMenuBtn {
                                id: btnAddRemove
                                width: toggleBarContainer.width
                                text: qsTr("Add/Remove")
                                btnIconSource: "../images/svg_images/add_business_white_24dp.svg"
                                onClicked: {
                                    btnHome.isActiveMenu = false
                                    btnSell.isActiveMenu = false
                                    btnBuy.isActiveMenu = false
                                    btnAddRemove.isActiveMenu = true
                                    btnStats.isActiveMenu = false
                                    btnHelp.isActiveMenu = false
                                    pageHome.visible = false
                                    pageSell.visible = false
                                    pageBuy.visible = false
                                    pageAddRemove.visible = true
                                    pageStats.visible = false
                                    pageHelp.visible = false
                                }
                            }

                            LeftMenuBtn {
                                id: btnStats
                                width: toggleBarContainer.width
                                text: qsTr("Statistics")
                                btnIconSource: "../images/svg_images/insights_white_24dp.svg"
                                onClicked: {
                                    btnHome.isActiveMenu = false
                                    btnSell.isActiveMenu = false
                                    btnBuy.isActiveMenu = false
                                    btnAddRemove.isActiveMenu = false
                                    btnStats.isActiveMenu = true
                                    btnHelp.isActiveMenu = false
                                    pageHome.visible = false
                                    pageSell.visible = false
                                    pageBuy.visible = false
                                    pageAddRemove.visible = false
                                    pageStats.visible = true
                                    pageHelp.visible = false
                                }
                            }
                        }

                        LeftMenuBtn {
                            id: btnHelp
                            width: toggleBarContainer.width
                            text: qsTr("Help")
                            anchors.bottom: parent.bottom
                            anchors.bottomMargin: 25
                            btnIconSource: "../images/svg_images/help_white_24dp.svg"
                            onClicked: {
                                btnHome.isActiveMenu = false
                                btnSell.isActiveMenu = false
                                btnBuy.isActiveMenu = false
                                btnAddRemove.isActiveMenu = false
                                btnStats.isActiveMenu = false
                                btnHelp.isActiveMenu = true
                                pageHome.visible = false
                                pageSell.visible = false
                                pageBuy.visible = false
                                pageAddRemove.visible = false
                                pageStats.visible = false
                                pageHelp.visible = true
                            }
                        }
                    }


                }
            }
        }
    }




    //DropShadow
    //Disabled
    DropShadow{
        anchors.fill: mouseAreaContainer
        horizontalOffset: 0
        verticalOffset: 4
        radius: 10
        samples: 16
        color: "#1b2129"
        source: bg
        z: 0
        visible:false
    }





    MouseArea {
        id: resizeLeft
        width: 5
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.LeftEdge)}
        }
    }

    MouseArea {
        id: resizeRight
        width: 5
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.RightEdge)}
        }
    }

    MouseArea {
        id: resizeBottom
        height: 5
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.BottomEdge)}
        }
    }

    MouseArea {
        id: resizeTop
        height: 5
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.TopEdge)}
        }
    }


    MouseArea {
        id: resizeBottomRight
        width: 20
        height: 20
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeFDiagCursor
        DragHandler {
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.RightEdge | Qt.BottomEdge)}
        }
    }

    MouseArea {
        id: resizeBottomLeft
        width: 20
        height: 20
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeFDiagCursor
        DragHandler {
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.LeftEdge | Qt.BottomEdge)}
        }
    }

    MouseArea {
        id: resizeTopLeft
        width: 20
        height: 20
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeFDiagCursor
        DragHandler {
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.LeftEdge | Qt.TopEdge)}
        }
    }

    MouseArea {
        id: resizeTopRight
        width: 20
        height: 20
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeFDiagCursor
        DragHandler {
            target: null
            onActiveChanged: if(active) {mainWindow.startSystemResize(Qt.RightEdge | Qt.TopEdge)}
        }
    }

}


