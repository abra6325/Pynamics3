import yik
def init(script):
    print("script initialization")
    print("parent: "+str(script.parent))
    print(script)
    bus = script.root.bus
    @bus.event_subscriber(yik.EVENTS.ADD_CHILD)
    def event_test_1(e:yik.AddChildEvent):
        e.success = True
        print("here we activate from the script")
