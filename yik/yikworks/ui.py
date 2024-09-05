import pathlib
import sys
import threading
import time

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QStyleFactory, QGridLayout
from qtpy import uic

from ..interface import YikObject


class QYikWorksUIMain(QMainWindow):

    tree: QTreeView = None

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

    def __init_sidebar__(self):
        self.side_top = QStandardItemModel(self)
        self.side_top.setHorizontalHeaderLabels(["Object", "Description"])

        self.tree.setModel(self.side_top)

        self.tree.header().resizeSection(0, 100)




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
