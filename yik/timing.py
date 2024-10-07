import multiprocessing
import threading
import time
from typing import Callable, Any

from .interface import YikObject, _PynamicsObjTyping
from .logger import Logger




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

class FakeThread:

    """Debug Purpose"""

    def cancel(self):
        return

class Routine(YikObject):

    """Has the ability to call itself and call all routines of its parent's children"""

    _yikworks_helper_iconpath = "object_routine.ico"

    def __init__(self, parent, target: Callable[[Any], Any] = None, initialize=None, frequency: int = 1,
                 start_delay: float = 1):
        """
        :param target: Target callable process.
        :param delay: Time to wait for another call. Measured in seconds.
        :param start_delay: Time to wait before the first tick is executed.
        """


        super().__init__(parent)

        self.threading_id = None
        self.target = target
        self.initialize = initialize
        self.frequency = frequency
        self.start_delay = start_delay

        self.calibration_sleep = 1

        self.calibration_sleep_interval_a = 0

        self._debug_ticks_completed = 0

    def _wrapper_target(self):
        self.target(self)
        #thread.cancel()

    def _loop_after(self, re=0):


        if re == self.frequency:
            return
        thread = threading.Timer(interval=1 / self.frequency, function=lambda: self._loop_after(re + 1))
        thread.start()

        self._wrapper_target()
        self._debug_ticks_completed += 1


    def _loop_first_thread(self, amount=0):
        self.calibration_sleep_interval_a = time.time()
        self._loop_after(re=amount)
        self.calibration_sleep_interval_b =time.time()

    def _loop(self):
        x = threading.Thread(target=lambda: self._loop_first_thread(amount=64))
        x.start()
        while True:
            x = threading.Thread(target=self._loop_first_thread)
            x.start()
            time.sleep(self.calibration_sleep)
            print(self._debug_ticks_completed)
            self._debug_ticks_completed = 0


    def start(self):
        """
        Asynchronous. Starts ticking this routine.
        :return: None
        """

        n = threading.Thread(target=self._loop)
        n.start()

    def __pn_repr__(self):
        return f"{self.__class__.__name__}(parent={self.parent})"


class CanTick(YikObject):
    """
    Use as enum flag
    """

    _routine = None

    def __init__(self, parent: _PynamicsObjTyping, *args, **kwargs):
        YikObject.__init__(self, parent, *args, **kwargs)

    def __post_init__(self, parent: _PynamicsObjTyping, routine_include=False, routine_frequency=128, routine_target=None):


        if routine_include:
            if routine_target is None:
                self._routine = Routine(self, frequency=routine_frequency, target=self.__pn_routine_update__)
            else:
                self._routine = Routine(self, frequency=routine_frequency, target=routine_target)
        else:
            if self._routine is not None:
                return
            self._routine = None

    def __pn_routine_update__(self, routine: Routine = None):
        """
        Default update function.
        :return:
        """
        pass

    def routine_launch(self):

        if self._routine is not None:
            self._routine.start()
        else:
            Logger.warn(f"{self} skipping routine_launch() since there are no available routines.")
