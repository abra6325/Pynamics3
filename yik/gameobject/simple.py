from ..interface import YikObject
from ..render import Renderable


class GameObject(Renderable):

    def __init__(self, parent, update=None):
        """

        :param parent: The parent of this object
        :param update: A callable function for this object's routine target. Set to None if this object does not tick.
        """
        super().__init__(parent)



