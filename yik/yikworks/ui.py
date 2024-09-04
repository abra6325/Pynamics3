
import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QMainWindow

from ..interface import YikObject

class QYikWorksUIMain(QMainWindow):

    def __init__(self, parent=None, yik_parent=None, yik_root=None):
        super().__init__(parent)

        self.setWindowTitle(f"YikWorks (Python 3.8.9) (YikEngine 0.8.11237742) {yik_root}")

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

        self.window = QYikWorksUIMain(yik_parent=self, yik_root=self.parent)
        self.window.show()
        self.app.exec()