from .interface import YikObject, _PynamicsObjTyping
from enum import Enum

def event_bus_subscriber(subscriber_class):
    orig_init = subscriber_class.__init__
    def __init__(self,id, *args, **kwargs):
        pass
class EVENTS(Enum):
    TICK = 1
    ADD_CHILD = 2


class EventBus(YikObject):
    def __init__(self, root, parent: _PynamicsObjTyping, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.bus = {}
        for i in [_.value for _ in EVENTS]:
            self.bus[i] = list()







