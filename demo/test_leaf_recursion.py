import yik
yik.set_naming_seed(224142)


print("Create NULL")
a = yik.NullObject()
print("Create GL")
y = yik.WindowGLTk(a)
print("Create WORLD")
x = yik.World(y)

print("Create OBJECT")
obj = yik.RenderableGameObject(x)
y.show()
y.launch()