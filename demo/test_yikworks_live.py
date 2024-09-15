import yik
yik.set_naming_seed(224142)


print("Create NULL")
a = yik.ApplicationObject("TestApp: App")
e = yik.EventBus(a)
print(a.children)
root = yik.YikWorksUI(a)
print("Create GL")
y = yik.WindowGLTk(a)
print("Create WORLD")
x = yik.World(y)

print("Create OBJECT")
obj = yik.RenderableGameObject(x)




a.show()

root.launch()
y.launch()