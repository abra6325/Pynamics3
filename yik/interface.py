import traceback
from enum import Enum
from typing import Set, Tuple

from .errors import OperationFail
from .events import EventHolder
from .logger import Logger

#from cik_core import CikObject

import uuid as ulib

class LeafOrder(Enum):
    ROOT_TO_LEAF = 0
    LEAF_TO_ROOT = 1

class _PynamicsObjTyping:
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

    _preserved_fields: Set[str] = set()
    _preserved_fields_locked: bool = False

    def __init__(self, parent: _PynamicsObjTyping, no_parent: bool = False, uuid: ulib.UUID = None):
        """
        :param parent: The parent of this object
        :param no_parent: `True` if this object does not have a parent. This will skip the parent initialization process.
        :param uuid: UUID of this object
        """
        super().__init__()
        self.uuid = uuid

        self.parent_callback = True

        self.children = []

        self.set_parent(parent)


        if self.uuid is None:
            self.uuid = ulib.uuid4()

        self.__post_init__()

    def __repr__(self):
        return f"[{self.__pn_repr__()}:{self.uuid}]"

    def __setattr__(self, key, value):
        if key in self._preserved_fields and self._preserved_fields_locked:

            raise OperationFail(
                f"Field \"{key}\" of type \"{self.__class__.__name__}\" is protected and read-only.")


        object.__setattr__(self, key, value)

    def __pn_repr__(self):
        return f"{self.__class__.__name__}"

    def __post_init__(self, *args, **kwargs):
        pass

    def __pre_leaf_added__(self, child, order=LeafOrder.LEAF_TO_ROOT):
        """
        Everytime a children is added to a object, this function will be called (as long self.parent_callback = True),
        and this function will recursively call its parent's __leaf_added__ function.

        This is the inner function of __leaf_added__ and act as a wrapper for the __leaf_added__ API function.
        :param order:
        :return:
        """



        if self.parent is not None and order == LeafOrder.ROOT_TO_LEAF:
            self.parent.__pre_leaf_added__(child, order)

        self.__leaf_added__(child)

        if self.parent is not None and order == LeafOrder.LEAF_TO_ROOT:
            self.parent.__pre_leaf_added__(child, order)

        pass

    def __leaf_added__(self, child):
        """
        This function will be called when a object that is this object's leaf is added.
        NOTE: THE OBJECT ITSELF __leaf_added__ FUNCTION WILL ALSO BE CALLED.

        :param child: The children that is being added as a leaf
        :return: None
        """

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

        if self.parent_callback:
            self.__pre_leaf_added__(self)

    def debug_unhighlight(self):
        pass

    def debug_highlight(self):
        pass

    def lock_fields(self):
        """
        Locks all the fields in self._preserved_fields
        :return:
        """
        self._preserved_fields_locked = True

    def unlock_fields(self):
        """
        Unlocks all the fields in self._preserved_fields
        :return:
        """
        self._preserved_fields_locked = False

    def update(self):
        pass

    def delete(self):
        pass


class NullObject(YikObject):
    """An object that has no parent and has no function in engine logic. Could be used as a parent during testing"""

    def __init__(self):
        super().__init__(None, no_parent=True)
