import random, time, threading


def worker1(file_list):
    for i in file_list:
        print(f"Worker1 started on {i}")
        time.sleep(random.randint(1, 4))
        print(f"Worker1 finished on {i}")