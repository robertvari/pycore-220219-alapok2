import random, time, threading


def worker1():
    print(f"Worker1 started on {threading.current_thread().name}")
    time.sleep(random.randint(1, 10))
    print(f"Worker1 finished on {threading.current_thread().name}")


def worker2():
    print(f"Worker2 started on {threading.current_thread().name}")
    time.sleep(random.randint(1, 10))
    print(f"Worker2 finished on {threading.current_thread().name}")


t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()

print(f"Hello! on {threading.current_thread().name}")