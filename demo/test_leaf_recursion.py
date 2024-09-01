import yik


print("Create NULL")
a = yik.NullObject()
print("Create GL")
y = yik.WindowGLTk(a)
print("Create WORLD")
x = yik.World(y)

print("Create OBJECT")
obj = yik.GameObject(x)