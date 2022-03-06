import random, time
from utilities.decorators import timer, useless_decorator


@timer
def worker1(sleep_time):
    print("Worker1 started")
    time.sleep(sleep_time)
    print("Worker1 finished")

    return sleep_time


@timer
def worker2():
    print("Worker2 started")
    time.sleep(random.randint(1, 10))
    print("Worker2 finished")


@timer
def worker3():
    print("Worker3 started")
    time.sleep(random.randint(1, 10))
    print("Worker3 finished")


result = worker1(3)
print(result)