import QtQuick 2.0
import QtQuick.Controls 2.15

Item {
    Rectangle {
        id: rectangle
        color: "#222831"
        anchors.fill: parent

        Label {
            id: label
            x: 284
            y: 177
            color: "#ececec"
            text: "Sell Page"
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 10
            font.family: "Seogue UI"
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

}

