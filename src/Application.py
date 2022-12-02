import sys

from qasync import QEventLoop
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from asyncio import BaseEventLoop

class Application:
    engine: QQmlApplicationEngine
    app: QGuiApplication
    loop: BaseEventLoop

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loop = QEventLoop(self.app)
        self.engine = QQmlApplicationEngine()

    def load_qml(self, qml: str):
        self.engine.load(qml)

    def run(self):
        if self.engine.rootObjects():
            with self.loop:
                self.loop.run_forever()
        else:
            sys.exit(-1)
