from typing import Any

from .interface import YikObject
from .logger import Logger
from .render import WindowGLTk

import threading
import time

from .timing import sleep, Routine, tps_to_seconds


class World(YikObject):
    n = 0

    def __init__(self, parent, tps=128):

        super().__init__(parent)

        self.tick = Routine(self, self._tick, delay=tps_to_seconds(tps))

        self._viewport: Any[WindowGLTk, None] = None

    def _tick(self):
        self.n += 1



    def launch(self):
        self.tick.start()

        if self._viewport is None:
            Logger.warn("No window created for this context. Skipping window startup.")
        else:
            #self._viewport.frame.start()
            self._viewport.load()

