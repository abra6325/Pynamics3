import threading
import time

import yik





x = yik.World(yik.NullObject())
y = yik.WindowGLTk(x)
def k():
    global x
    while True:
        print(x.n)
        x.n = 0
        time.sleep(1)
j = threading.Thread(target=k)
j.start()

x.launch()