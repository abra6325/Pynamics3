from .interface import YikObject, _IApplicationObject


class ApplicationObject(YikObject, _IApplicationObject):
    def __init__(self, app_id: str):
        YikObject.__init__(self, None, no_parent=True)
        self.app_id = app_id

        self.yikworks = None
        self.bus = None
        self.root = self
