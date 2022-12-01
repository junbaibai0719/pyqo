import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication


class Application:
    engine: QQmlApplicationEngine
    app: QGuiApplication

    def __init__(self):
        self.app = QApplication()
        self.engine = QQmlApplicationEngine()

    def load_qml(self, qml: str):
        self.engine.load(qml)

    def run(self):
        if self.engine.rootObjects():
            sys.exit(self.app.exec())
        else:
            sys.exit(-1)
