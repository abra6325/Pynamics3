import yik
yik.set_naming_seed(224142)

a = yik.ApplicationObject("RenderTestApplication")

root = yik.YikWorksUI(a)

y = yik.WindowGLTk(a)

x = yik.World(y)

obj = yik.RenderableGameObject(x)
obj2 = yik.RenderableGameObject(x)
obj3 = yik.RenderableGameObject(x)

root.launch()

y.launch()