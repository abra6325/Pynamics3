from typing import Set, Tuple

from .errors import OperationFail
from .events import EventHolder
from .logger import Logger

from cik_core import CikObject

import uuid as ulib


class _PynamicsObjTyping():
    children: list = None
    parent = None

    def add_children(self, obj): pass

    def set_parent(self, obj): pass

    def delete(self): pass


class YikObject(_PynamicsObjTyping):
    _children_blacklist: Tuple[type] = tuple()
    _children_whitelist: Tuple[type] = tuple()

    _parent_whitelist: Tuple[type] = tuple()
    _parent_blacklist: Tuple[type] = tuple()

    def __init__(self, parent: _PynamicsObjTyping, no_parent: bool = False, uuid: ulib.UUID = None):
        """
        :param parent: The parent of this object
        :param no_parent: `True` if this object does not have a parent. This will skip the parent initialization process.
        :param uuid: UUID of this object
        """
        super().__init__()
        self.uuid = uuid

        self.children = []

        self.set_parent(parent)


        if self.uuid is None:
            self.uuid = ulib.uuid4()

        self.__post_init__()

    def __repr__(self):
        return f"[{self.__pn_repr__()}:{self.uuid}]"

    def __pn_repr__(self):
        return f"{self.__class__.__name__}"

    def __post_init__(self, *args, **kwargs):
        pass

    def unbind(self):
        self.parent.children.remove(self)

    def add_children(self, obj):


        if len(self._children_whitelist) != 0:
            if not isinstance(obj, self._children_whitelist):
                s = ", ".join(map(lambda i: i.__name__, self._children_whitelist))
                Logger.error_exc(OperationFail(
                    f"type \"{self.__class__.__name__}\" only supports the following children types: {s}"), description=f"In {self} loading {obj}")
                return

        if isinstance(obj, self._children_blacklist):
            s = ", ".join(map(lambda i: i.__name__, self._children_blacklist))
            Logger.error_exc(OperationFail(
                f"type \"{self.__class__.__name__}\" disallows the following children types: {s}"), description=f"In {self} loading {obj}")
            return

        self.children.append(obj)
        obj.parent = self

    def set_parent(self, obj):

        if obj is None : return

        if len(self._parent_whitelist) != 0:
            s = ", ".join(map(lambda i: i.__name__, self._parent_whitelist))
            if not isinstance(obj, self._parent_whitelist):
                Logger.error_exc(OperationFail(
                    f"type \"{self.__class__.__name__}\" only supports the following parent types: {s}"), description=f"Loading {self}")
                return

        if isinstance(obj, self._parent_blacklist):
            s = ", ".join(map(lambda i: i.__name__, self._parent_blacklist))
            Logger.error_exc(OperationFail(
                f"type \"{self.__class__.__name__}\" disallows the following parent types: {s}"), description=f"Loading {self}")
            return

        obj.add_children(self)
        self.parent = obj

    def debug_unhighlight(self):
        pass

    def debug_highlight(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class NullObject(YikObject):
    """An object that has no parent and has no function in engine logic. Could be used as a parent during testing"""

    def __init__(self):
        super().__init__(None, no_parent=True)
