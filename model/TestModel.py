from PySide6.QtGui import QStandardItemModel
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "test"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class TestModel(QStandardItemModel):
    ...
