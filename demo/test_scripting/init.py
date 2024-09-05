import yik

yik.set_naming_seed(66777888) # makes sure all naming references are the same

print("Create NULL")
a = yik.ApplicationObject("test_engine")

print("Create GL")
e = yik.EventBus(a)

@e.event_subscriber(yik.EVENTS.ADD_CHILD)
def test1(e):
    print(e)
    e.success = True
    print(e.parent)



print("Created Event Bus")
y = yik.WindowGLTk(a)
print("Create WORLD")
x = yik.World(y)
x.launch()
print(x.root.app_id)
print("Create OBJECT")
obj = yik.RenderableGameObject(x)
x.attach_script("test_aa")
#.show()
y.launch()