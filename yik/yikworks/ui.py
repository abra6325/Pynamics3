import pathlib
import sys
import threading
import time

from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QFont, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QStyleFactory, QGridLayout, QLabel, QStyle
from qtpy import uic

from ..interface import YikObject

ITALIC_FONT = QFont()
ITALIC_FONT.setItalic(True)

BOLD_FONT = QFont()
BOLD_FONT.setBold(True)

NATIVE_CODE = QFont()
NATIVE_CODE.setItalic(True)


def fullname(o):
    klass = o
    module = klass.__module__
    if module == 'builtins':
        return klass.__qualname__  # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__


class QYikWorksUIMain(QMainWindow):
    tree: QTreeView = None
    property_tree: QTreeView = None

    def __init__(self, parent=None, yik_parent=None, yik_root=None):
        super().__init__(parent)

        # self.setWindowTitle(f"YikWorks (Python 3.8.9) (YikEngine 0.8.11237742) {yik_root}")
        # self.resize(1200, 675)
        #
        # self.statusBar().showMessage("Hello Yikworks World!")
        #
        # self.layout = QGridLayout()
        # self.layout.setSpacing(10)
        #
        # self.__init_sidebar__()
        #
        # self.setLayout(self.layout)

        self.root = yik_root

        x = pathlib.Path(__file__).parent.joinpath("uic").joinpath("MainWindow.ui").resolve()
        uic.loadUi(x, self)

        self.setWindowTitle(f"YikWorks 1.0 {self.root}")

        self.__init_sidebar__()
        self.side_top.children_counter = 0

        self.tree_ref = {}
        self._root_recursion(self.root, self.side_top, self.side_top)

        self.tree.selectionModel().currentChanged.connect(self._treeview_instance_changed)

    def _root_recursion(self, starter, item_parent, root):

        self.tree_ref[starter.name] = starter

        item = QStandardItem(f"{starter.name}")  # col 0 in header actually

        x = pathlib.Path(__file__).parent.joinpath("icons").joinpath(
            starter.__class__._yikworks_helper_iconpath).resolve()
        item.setIcon(QIcon(str(x)))

        item.setEditable(False)
        item_parent.appendRow(item)
        item.children_counter = 0

        if isinstance(item_parent, QStandardItemModel):
            item_parent.setItem(item_parent.children_counter, 1, QStandardItem(f"{starter.__class__.__name__}"))
            item_parent.setItem(item_parent.children_counter, 2, QStandardItem(f"{starter}"))
        else:
            item_parent.setChild(item_parent.children_counter, 1, QStandardItem(f"{starter.__class__.__name__}"))
            item_parent.setChild(item_parent.children_counter, 2, QStandardItem(f"{starter}"))
        item_parent.children_counter += 1

        # self.side_top.setItem()

        if len(starter.children) == 0:
            return
        for i in starter.children:
            self._root_recursion(i, item, root)

    def _treeview_instance_changed(self, current: QModelIndex, previous):

        cur = self.tree_ref[current.data()]

        self.property_top.clear()
        self.property_top.setHorizontalHeaderLabels(["Property", "Type", "Content"])
        self._treeview_iterate_properties(cur)

    def _treeview_iterate_properties(self, object):

        item = QStandardItem(f"Object Attributes")
        item.setFont(BOLD_FONT)
        item.setBackground(QBrush(QColor(50, 200, 50)))
        self.property_top.appendRow(item)

        d = object.__dict__
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}

        for i in d:
            item2 = QStandardItem(str(i))
            item2_tooltip = str(i)

            typing_function = QStandardItem(str(d[i]))
            typing_function_tooltip = str(d[i])

            typing_function_sec = QStandardItem(d[i].__class__.__name__)
            typing_function_sec_tooltip = d[i].__class__.__name__

            if i.startswith("children"):
                typing_function.setText("[Child Array]")
                typing_function.setFont(NATIVE_CODE)
                typing_function.setForeground(QBrush(QColor(128, 0, 128)))

            if i.startswith("_"):
                item2.setForeground(QBrush(QColor(196, 196, 196)))
                item2.setFont(ITALIC_FONT)

                typing_function_sec.setForeground(QBrush(QColor(196, 196, 196)))
                typing_function_sec.setFont(ITALIC_FONT)

                typing_function.setForeground(QBrush(QColor(196, 196, 196)))
                typing_function.setFont(ITALIC_FONT)

                item2_tooltip += f"\n\nThis is a protected member of the object {object}"
                typing_function_tooltip += f"\n\nThis is a protected member of the object {object}"
                typing_function_sec_tooltip += f"\n\nThis is a protected member of the object {object}"

            item2.setToolTip(item2_tooltip)
            typing_function.setToolTip(typing_function_tooltip)
            typing_function_sec.setToolTip(typing_function_sec_tooltip)

            item.appendRow(item2)
            item.setChild(item2.index().row(), 1, typing_function_sec)
            item.setChild(item2.index().row(), 2, typing_function)

        for i in object.__class__.__mro__:
            item = QStandardItem(f"{i.__name__} ({fullname(i)})")
            item.setFont(BOLD_FONT)
            item.setBackground(QBrush(QColor(255, 200, 100)))
            self.property_top.appendRow(item)

            cook = vars(i)
            cook_list = list(cook)
            cook_list.sort()

            for j in cook_list:

                item2 = QStandardItem(j)
                item2_tooltip = str(j)

                typing_function = QStandardItem(str(cook[j]))
                typing_function_tooltip = str(cook[j])

                typing_function_sec = QStandardItem(cook[j].__class__.__name__)
                typing_function_sec_tooltip = cook[j].__class__.__name__

                if j.startswith("_"):
                    item2.setForeground(QBrush(QColor(196, 196, 196)))
                    item2.setFont(ITALIC_FONT)

                typing_function = QStandardItem()

                if callable(cook[j]):
                    typing_function.setText("[Python Code]")
                    typing_function.setFont(NATIVE_CODE)
                    typing_function.setForeground(QBrush(QColor(0, 128, 0)))
                    typing_function_tooltip += "\n\nThis is a callable python function.\nYou can select this row and and use Debug > Call Attribute to run this function"
                elif j == "__doc__":
                    typing_function.setText("[Documentation]")
                    typing_function.setFont(ITALIC_FONT)
                    typing_function.setForeground(QBrush(QColor(0, 0, 128)))
                    typing_function_tooltip += "\n\nThis is the documentation for this object"
                elif isinstance(cook[j], bool):
                    typing_function.setText(str(cook[j]))
                    # self.property_tree.setItemDelegateForRow()
                else:
                    typing_function.setText(str(cook[j]))

                item2.setToolTip(item2_tooltip)
                typing_function.setToolTip(typing_function_tooltip)
                typing_function_sec.setToolTip(typing_function_sec_tooltip)

                item.appendRow(item2)
                item.setChild(item2.index().row(), 1, typing_function_sec)
                item.setChild(item2.index().row(), 2, typing_function)

        self.property_tree.expandAll()

    def __init_sidebar__(self):
        self.side_top = QStandardItemModel(self)
        self.side_top.setHorizontalHeaderLabels(["Object", "Class", "Description"])

        self.tree.setModel(self.side_top)

        self.tree.header().resizeSection(0, 240)
        self.tree.header().resizeSection(1, 120)
        self.tree.header().resizeSection(2, 640)
        self.tree.setStyle(QStyleFactory.create('windows'))

        self.property_top = QStandardItemModel(self)
        self.property_top.setHorizontalHeaderLabels(["Property", "Type", "Content"])

        self.property_tree.setModel(self.property_top)
        self.property_tree.header().resizeSection(0, 100)


class YikWorksUI(YikObject):

    def __init__(self, parent):
        YikObject.__init__(self, parent)
        self.app = None

    def launch(self):
        threading.Thread(target=self._launch_wrapper).start()

    def _launch_wrapper_test(self):
        self.window.setWindowTitle("ARGARG")

    def _launch_wrapper(self):
        self.app = QApplication(sys.argv)

        self.window = QYikWorksUIMain(yik_parent=self, yik_root=self.parent.root)
        self.window.show()
        self.app.exec()
