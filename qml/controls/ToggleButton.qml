import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button {
    id:toggleButton
    width: 55
    height: 55

    //Custom Properties
    property url btnIconSource: "../../images/svg_images/menu_white_24dp.svg"
    property color btnColorDefault: "#1b2129"
    property color btnColorMouseOver: "#30475e"
    property color btnColorClicked: "#1b2129"
    QtObject{
        id:internal

        //Mouse Over and Clicked
        property var dynamicColor:if(toggleButton.down){
                                      toggleButton.down?btnColorClicked:btnColorDefault
                                  }else{
                                      toggleButton.hovered?btnColorMouseOver:btnColorDefault
                                  }
    }

    implicitWidth : 55
    implicitHeight : 55

    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor
        radius: 10

        Image{
            id: iconBtn
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Image.AlignHCenter
            verticalAlignment: Image.AlignVCenter
            source: btnIconSource
            anchors.horizontalCenter: parent.horizontalCenter
            height:30
            width:30
            fillMode: Image.PreserveAspectFit
        }

        ColorOverlay{
            anchors.fill:iconBtn
            source: iconBtn
            color: "#ececec"
            antialiasing: false
        }
    }

}



/*##^##
Designer {
    D{i:0;height:55;width:55}
}
##^##*/
