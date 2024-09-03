from typing import overload

from ..interface import YikObject
from ..render import Renderable
from ..script import ScriptableObject
from ..timing import CanTick

class RenderableGameObject(Renderable, CanTick, ScriptableObject):

    def __init__(self, parent, routine_include=False):
        """

        :param parent: The parent of this object
        :param update: A callable function for this object's routine target. Set to None if this object does not tick.
        """
        Renderable.__init__(self, parent)
        CanTick.__init__(self, parent, primary_initialization=False, routine_include=routine_include)
        ScriptableObject.__init__(self, parent, primary_initialization=False)

    def _routine_update(self, e):
        #print(e)
        pass



