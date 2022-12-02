// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

import test

ApplicationWindow {
    id: window
    width: 360
    height: 520
    visible: true
    title: "Qt Quick Controls"

    TestModel{
        id: testModel
        Component.onCompleted:{
            console.log(11111111111)
        }
    }

    Column {
        Button {
            id: syncBtn
            text: "同步按钮"
            onClicked:{
                testModel.sync()
            }
        }

        Button {
            id: asyncBtn
            text: "异步按钮"
            onClicked:{
                testModel.async_req()
            }
        }
    }
}