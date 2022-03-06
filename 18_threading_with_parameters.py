from utilities.file_utils import get_files
import random, time, threading

# get all photos from root_folder
root_folder = r"C:\Work\_PythonSuli\pycore-220219\photos"
photo_list = []
get_files(
    root_folder=root_folder,
    files=photo_list
)


def worker1(file_list):
    for i in file_list:
        print(f"Worker1 started on {i}")
        time.sleep(random.randint(1, 4))
        print(f"Worker1 finished on {i}")


t1 = threading.Thread(target=worker1, args=[photo_list])
t1.start()