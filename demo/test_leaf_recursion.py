import yik
yik.set_naming_seed(224142)


print("Create NULL")
a = yik.ApplicationObject("11")

root = yik.YikWorksUI(a)

e = yik.EventBus(a)


@e.event_subscriber(yik.EVENTS.ADD_CHILD)
def test1(e: yik.AddChildEvent):
    print(e)
    e.success = True
print("Create GL")
y = yik.WindowGLTk(a)
print("Create WORLD")
x = yik.World(y)

print("Create OBJECT")
obj = yik.RenderableGameObject(x)
y.show()
y.launch()