import yik
from yik.dimensions import Dimension
from yik.timing import CanTick

yik.set_naming_seed(224142)

a = yik.ApplicationObject("RenderTestApplication")

root = yik.YikWorksUI(a)

y = yik.WindowGLTk(a)

x = yik.World(y, tps=128)

obj = yik.Particle(x)

print(isinstance(obj, CanTick))
obj.position = Dimension(100, 50)
obj.velocity = Dimension(0.5, -0.05)
obj.constant_acceleration = Dimension(0, 0.002)

root.launch()

import time
time.sleep(1)

y.launch()