import threading
import time

import yik




y = yik.WindowGLTk(yik.NullObject())
x = yik.World(y)

def k():
    global x
    while True:
        print(x.n)
        x.n = 0
        time.sleep(1)
j = threading.Thread(target=k)
j.start()

obj1 = yik.GameObject(x)
obj2 = yik.GameObject(obj1)

y.launch()