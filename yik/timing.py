import multiprocessing
import threading
import time
from typing import Callable, Any

from .interface import YikObject
from .logger import Logger

from .cik_core import sleep as cysleep


def sleep(seconds: float):
    a = time.time()
    b = a + seconds
    while time.time() < b:  # wait is your sleep time
        # print(time.time(), b)
        pass

    return

def sleep2(seconds: float):
    pass


def tps_to_seconds(tps: int) -> float:
    return 1 / tps

class Timer:

    @staticmethod
    def init():
        import ctypes
        kernel32 = ctypes.windll.kernel32

        # This sets the priority of the process to realtime--the same priority as the mouse pointer.
        kernel32.SetThreadPriority(kernel32.GetCurrentThread(), 31)
        # This creates a timer. This only needs to be done once.
        timer = kernel32.CreateWaitableTimerA(ctypes.c_void_p(), True, ctypes.c_void_p())
        # The kernel measures in 100 nanosecond intervals, so we must multiply .25 by 10000
        delay = ctypes.c_longlong(int(1000 * 10000))
        kernel32.SetWaitableTimer(timer, ctypes.byref(delay), 0, ctypes.c_void_p(), ctypes.c_void_p(), False)
        kernel32.WaitForSingleObject(timer, 0xffffffff)

        print("TEST2")


class Routine(YikObject):

    def __init__(self, parent, target: Callable[[Any], Any] = None, initialize=None, delay: float = 1, start_delay: float = 1):
        """
        :param target: Target callable process.
        :param delay: Time to wait for another call. Measured in seconds.
        :param start_delay: Time to wait before the first tick is executed.
        """
        super().__init__(parent)

        if delay < (1/64):
            Logger.warn(f"{self} : The universal minimal resolution for time.sleep is 1/64 seconds (You specified {1 / delay}). Some systems may "
                        f"have the TPS capped at 64.")

        self.threading_id = None
        self.target = target
        self.initialize = initialize
        self.delay = delay
        self.start_delay = start_delay

    def _loop(self):
        while True:
            self.target()
            #print("loop")
            cysleep(7812500, True)

    def start(self):
        """
        Asynchronous. Starts ticking this routine.
        :return: None
        """


        n = threading.Thread(target=self._loop)
        n.start()

    def __pn_repr__(self):
        return f"{self.__class__.__name__}(parent={self.parent})"
