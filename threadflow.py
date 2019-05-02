from threading import *

#threading workflow
class EvenNumbersThread:
    def __init__(self,val):
        self.max = val
    def display(self):
        for i in range(self.max):
            if i&1 == 0:
                print(i)

class OddNumbersThread:
    def __init__(self,val):
        self.max = val
    def display(self):
        for i in range(self.max):
            if i&1 != 0:
                print("  ",i)

E = EvenNumbersThread(100)
t1 = Thread(target=E.display)
                
O = OddNumbersThread(100)
t2 = Thread(target=O.display)

t1.start()
t2.start()

for j in range(100):
    print("   ",j)
