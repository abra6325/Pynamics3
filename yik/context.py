from typing import Any

from .gameobject.simple import GameObject
from .interface import YikObject
from .logger import Logger
from .render import WindowGLTk

import threading
import time

from .timing import sleep, Routine, tps_to_seconds


class World(YikObject):
    n = 0

    _parent_whitelist = (WindowGLTk,)
    _preserved_fields = {"_tick", "__tick"}

    def __init__(self, parent, tps=128):

        super().__init__(parent)

        self._tick = Routine(self, self.__tick, frequency=128)

        self._viewport = parent
        self.parent._context = self

        self.lock_fields()

    def __tick(self):
        self.n += 1



    def launch(self):
        self._tick.start()

        pass

