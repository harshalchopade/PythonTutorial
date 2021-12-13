from threading import *
from time import *

class A(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = A()
t2 = B()

t1.start()
sleep(2)
t2.start()

t1.join()
t2.join()

print("Bye")