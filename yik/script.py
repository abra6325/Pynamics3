import importlib

from .interface import YikObject


class ScriptObject(YikObject):
    def __init__(self, fpath: str, parent):
        super().__init__(parent)
        self.path = fpath
        self.script_as_module = importlib.import_module(self.path)
        self.script_as_module.init(self.parent)

class ScriptableObject(YikObject):

    def __post_init__(self, parent):
        pass

    def attach_script(self, fpath: str):
        """
        attaches script to object. Script must have an init() function.
        BEWARE OF NAME OVERLAP WITH OTHER LIBRARIES
        :param fpath:
        :return:
        """
        tmp = ScriptObject(fpath, self)
        self.scripts.append(tmp)