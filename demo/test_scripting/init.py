import yik

yik.set_naming_seed(66777888) # makes sure all naming references are the same

print("Create NULL")
a = yik.NullObject()
print("Create GL")
y = yik.WindowGLTk(a)
print("Create WORLD")
x = yik.World(y)

print("Create OBJECT")
obj = yik.RenderableGameObject(x)
x.attach_script("test_aa")
#.show()
y.launch()