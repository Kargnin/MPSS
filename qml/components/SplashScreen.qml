import QtQuick 2.0
import QtQuick.Controls 2.15



    Frame{
        id: splashscreen
        width: 680
        height: 400
         property color bgColor: "#222831"
        //        focusPolicy: Qt.StrongFocus
        antialiasing: false
        font.weight: Font.Normal

        background: Rectangle {
            color: splashscreen.bgColor
            border.color: splashscreen.bgColor
            radius: 10
        }

        Text {
            id: text_title
            height: 60
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:28pt; color:#30475e;\">MPSS</span></p></body></html>"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 98
            anchors.leftMargin: 118
            textFormat: Text.RichText
            anchors.topMargin: 54
        }

        Text {
            id: text_subtitle
            height: 30
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; color:#ececec;\">Group 8: 19CS10020 19CS10034 19CS30046</span></p></body></html>"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: text_title.bottom
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 15
            anchors.leftMargin: 35
            textFormat: Text.RichText
            anchors.topMargin: 13
        }

        Text {
            id: text_loading
            x: 158
            y: 238
            width: 132
            height: 30
            text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:8pt; color:#ececec;\">Loading......</span></p></body></html>"
            anchors.top: progressbar.bottom
            anchors.bottom: parent.bottom
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.horizontalCenterOffset: 42
            anchors.bottomMargin: 88
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 6
            textFormat: Text.RichText
        }

        BusyIndicator {
            id: busyIndicator
            x: 242
            y: 253
            width: 40
            height: 40
            anchors.right: text_loading.left
            anchors.bottom: parent.bottom
            anchors.rightMargin: 22
            anchors.bottomMargin: 83
//            background: Rectangle {
//                color: splashscreen.BGColor
//                border.color: splashscreen.BGColor
//                radius: 10
//            }


                contentItem: Item {
                    implicitWidth: 64
                    implicitHeight: 64

                    Item {
                        id: item1
                        opacity: control.running ? 1 : 0
                        anchors.fill: parent
                        anchors.leftMargin: -7
                        anchors.topMargin: -4
                        anchors.rightMargin: -6
                        anchors.bottomMargin: -4


                        Repeater {
                            id: repeater
                            model: 6

                            Rectangle {
                                x: item1.width / 2 - width / 2
                                y: item1.height / 2 - height / 2
                                implicitWidth: 10
                                implicitHeight: 10
                                radius: 5
                                color: "#f2a365"
                                transform: [
                                    Translate {
                                        y: -Math.min(item1.width, item1.height) * 0.5 + 5
                                    },
                                    Rotation {
                                        angle: index / repeater.count * 360
                                        origin.x: 5
                                        origin.y: 5
                                    }
                                ]
                            }
                        }
                    }
                }
        }

    }




/*##^##
Designer {
    D{i:0;formeditorZoom:1.25}
}
##^##*/
