# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.4.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore
from model import TestModel
qt_resource_data = b"\
\x00\x00\x01\xaa\
/\
/ Copyright (C) \
2021 The Qt Comp\
any Ltd.\x0d\x0a// SPD\
X-License-Identi\
fier: LicenseRef\
-Qt-Commercial O\
R BSD-3-Clause\x0d\x0a\
\x0d\x0aimport QtQuick\
\x0d\x0aimport QtQuick\
.Layouts\x0d\x0aimport\
 QtQuick.Control\
s\x0d\x0a\x0d\x0aimport test\
\x0d\x0a\x0d\x0aApplicationW\
indow {\x0d\x0a    id:\
 window\x0d\x0a    wid\
th: 360\x0d\x0a    hei\
ght: 520\x0d\x0a    vi\
sible: true\x0d\x0a   \
 title: \x22Qt Quic\
k Controls\x22\x0d\x0a\x0d\x0a \
   TestModel{\x0d\x0a \
       Component\
.onCompleted:{\x0d\x0a\
            cons\
ole.log(11111111\
111)\x0d\x0a        }\x0d\
\x0a    }\x0d\x0a}\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x07\
\x08sX\xbc\
\x00A\
\x00p\x00p\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x84\xcd\xe3\xb1\xf3\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
