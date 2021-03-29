import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button {
    id:minimise
    width: 40
    height: 40

    implicitWidth : 40
    implicitHeight : 40

    property url btnIconSource:"../../images/svg_images/minimize_white_24dp.svg"
    property color btnColorDefault:"#1b2129"
    property color btnColorMouseOver:"#30475e"
    property color btnColorClicked:"#1b2129"
    QtObject{
        id:internal

        //Mouse Over and Clicked
        property var dynamicColor:if(minimise.down){
                                      minimise.down?btnColorClicked:btnColorDefault
                                  }else{
                                      minimise.hovered?btnColorMouseOver:btnColorDefault
                                  }
    }

    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor

        Image{
            id: iconBtn
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Image.AlignHCenter
            verticalAlignment: Image.AlignVCenter
            source: btnIconSource
            anchors.horizontalCenter: parent.horizontalCenter
            height:16
            width:16
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
    D{i:0;height:40;width:40}
}
##^##*/
