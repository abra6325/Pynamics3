import yik

yik.set_naming_seed(66777888)  # makes sure all naming references are the same

print("Create NULL")
a = yik.ApplicationObject("test_engine")
root = yik.YikWorksUI(a)
print("Create GL")
e = yik.EventBus(a)


@e.event_subscriber(yik.EVENTS.ADD_CHILD)
def test1(e: yik.AddChildEvent):
    print(e)
    e.success = True

print("Created Event Bus")
y = yik.WindowGLTk(a)
print("Create WORLD")
x = yik.World(y)
x.launch()
print("Create OBJECT")
obj = yik.RenderableGameObject(x)
x.attach_script("test_aa")

print("SHOWING WORLDS")
y.launch()