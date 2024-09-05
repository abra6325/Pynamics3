from .interface import YikObject, _PynamicsObjTyping
from .events_enum import EVENTS
from .event_arguments import EventArgument

from .application import ApplicationObject



class EventBus(YikObject):
    def __init__(self, root, *args, **kwargs):


        super().__init__(root, *args, **kwargs)
        self.parent.bus = self
        self.bus = {}
        for i in [_.value for _ in EVENTS]:
            self.bus[i] = list()

        print(self.bus)


    def event_subscriber(self, decorator_type: EVENTS):
        def inner(func):
            self.bus[decorator_type.value].append(func)
            self.trigger_event(EVENTS.ADD_EVENT, EventArgument())

            def wrapper(*args, **kwargs):
                func(*args, **kwargs)

            return wrapper

        return inner

    def trigger_event(self, event_type: EVENTS, event_args: EventArgument):
        funcs = self.bus[event_type.value]
        fails = []
        for i in funcs:
            i(event_args)
            success = event_args.success
            if not success:
                fails.append(i)
        return fails