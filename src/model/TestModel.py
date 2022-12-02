import asyncio
import time

import aiohttp as aiohttp
import qasync
import requests as requests
from PySide6.QtCore import Slot
from PySide6.QtGui import QStandardItemModel
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "test"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class TestModel(QStandardItemModel):
    ...

    @Slot()
    def sync(self):
        time.sleep(10)
        # with requests.get("http://baidu.com") as resp:
        #     print(resp.text)

    @qasync.asyncSlot()
    async def async_req(self):
        await asyncio.sleep(10)
        # async with aiohttp.request("get", "http://baidu.com") as resp:
        #     print(await resp.read())
