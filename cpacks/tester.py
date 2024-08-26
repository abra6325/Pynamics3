import cynamics
import faulthandler
import time
if __name__ == "__main__":

    faulthandler.enable() #start @ the beginning
start = time.time()
cnt = 0
while time.time() - start <= 1:
    cynamics.sleep(7812500,True)
    cnt+=1

print(cnt)


