
from time import*
import threading


def fun1():
    while True:
        print("Hello")
        sleep(1)


def fun2():
    while True:
        print("Bye")
        sleep(1)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

t1.start()
sleep(0.5)
t2.start()

t1.join()
t2.join()

print("Done")


