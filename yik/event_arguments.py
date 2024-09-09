class EventArgument:
    def __init__(self):
        self.success = False
        self.canceled = False

class AddChildEvent(EventArgument):
    def __init__(self,parent, child):
        super().__init__()
        self.parent = parent
        self.child = child