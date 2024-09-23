from typing import Any

from .interface import YikObject
from .logger import Logger
from .render import WindowGLTk
from .events_enum import EVENTS
from .event_arguments import EventArgument
import threading
import time

from .script import ScriptableObject
from .timing import sleep, Routine, tps_to_seconds, CanTick


class World(CanTick, ScriptableObject):
    n = 0

    _parent_whitelist = (WindowGLTk,)
    _preserved_fields = {"_tick", "__tick"}

    def __init__(self, parent, tps=128):
        CanTick.__init__(self, parent, routine_include=True, routine_frequency=tps)
        ScriptableObject.__init__(self, parent, primary_initialization=False)

        self._viewport = parent
        self.parent._context = self

        self._tickers = set()

        self.lock_fields()

    def __tick(self):
        #print("world tick")

        # self.root.bus.trigger_event(EVENTS.TICK,EventArgument()) Moved this line to timing.py handling routine ticks.
        # Why the fuck would u call tick event here? Routine is the one ticking not World u bozo.

        for i in self._tickers:
            i.__pn_routine_update__(self._routine)

    def __leaf_added__(self, child):
        if child is self: return

        if isinstance(child, CanTick):
            Logger.debug(f"{self} noticed CanTick {child}. Adding to routine tick list.")

            self._tickers.add(child)

    def __pn_routine_update__(self, routine: Routine = None):
        self.__tick()


    def launch(self):
        self.routine_launch()

