from utilities.file_utils import get_files
import threading, time, random, queue

# get all photos from root_folder
root_folder = r"C:\Work\_PythonSuli\pycore-220219\photos"
photo_list = []
get_files(
    root_folder=root_folder,
    files=photo_list
)

# create an empty job queue for threads
job_queue = queue.Queue()

# update queue with photo_list
for file in photo_list:
    job_queue.put(file)