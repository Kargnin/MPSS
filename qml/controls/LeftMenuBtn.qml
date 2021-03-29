import QtQuick 2.3
import QtQuick.Controls 2.3
import QtGraphicalEffects 1.15

Button {
    id:btnLeftMenu
    text:qsTr("Left Menu Text")

    //Custom Properties
    property url btnIconSource: "../../images/svg_images/menu_white_24dp.svg"
    property color btnColorDefault: "#1b2129"
    property color btnColorMouseOver: "#30475e"
    property color btnColorClicked: "#1b2129"
    property color activemenuColor: "#f2a365"
    property int iconwidth: 30
    property int iconheight: 30
    property bool isActiveMenu: false


    QtObject{
        id:internal

        //Mouse Over and Clicked
        property var dynamicColor:if(btnLeftMenu.down){
                                      btnLeftMenu.down?btnColorClicked:btnColorDefault
                                  }else{
                                      btnLeftMenu.hovered?btnColorMouseOver:btnColorDefault
                                  }
    }

    implicitWidth : 250
    implicitHeight : 55

    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor

        Rectangle{
            anchors{
                top:parent.top
                left: parent.left
                bottom: parent.bottom
            }
            color: activemenuColor
            width: 5
            visible: isActiveMenu
        }
    }

    contentItem: Item{
        id:content
        anchors.fill: parent

        Image{
            id: iconBtn

            source: btnIconSource
            anchors.leftMargin: 10
            sourceSize.height: iconheight
            sourceSize.width: iconwidth
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            width: iconwidth
            height: iconheight
            fillMode: Image.PreserveAspectFit
            visible: false

            antialiasing: true
        }

        ColorOverlay{
            anchors.fill: iconBtn
            source: iconBtn
            color: "#ececec"
            antialiasing: true
            width: iconwidth
            height:iconheight
        }

        Text{
            color: "#ececec"
            text: btnLeftMenu.text
            font: btnLeftMenu.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 70
            visible: true
        }

    }

}





/*##^##
Designer {
    D{i:0;height:60;width:250}D{i:5}D{i:6}
}
##^##*/
