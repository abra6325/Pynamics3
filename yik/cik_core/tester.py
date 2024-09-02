import cik_core
import faulthandler
import time
if __name__ == "__main__":

    faulthandler.enable() #start @ the beginning
start = time.time()
cnt = 0
children = cik_core.CikObject()
cikObj = cik_core.CikObject(children)
cikObj.add_child(children)
print(cikObj.children)
cik_core.sleep(100,True)
print(cnt)


