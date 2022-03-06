import os, time, threading, queue, shutil
from PIL import Image
from utilities.file_utils import get_files


THUMBNAIL_SIZE = 300
job_queue = queue.Queue()


def main():
    # get root_folder
    root_folder = get_root_folder()

    # delete _thumbnails folder
    thumbnail_folder_path = os.path.join(root_folder, "_thumbnails")
    if os.path.exists(thumbnail_folder_path):
        shutil.rmtree(thumbnail_folder_path, ignore_errors=True)

    # collect all photos from root_folder and subfolders
    photo_files = collect_photos(root_folder)

    # update job queue
    [job_queue.put(i) for i in photo_files]

    # create thumbnail_folder
    thumbnail_folder = create_thumbnail_folder(root_folder)

    # convert images to thumbnails
    for _ in range(6):
        t = threading.Thread(target=thumbnail_worker, args=[thumbnail_folder])
        t.start()


def get_root_folder():
    # root_folder = input("Where are your photos?")

    # todo remove this!
    root_folder = r"C:\Work\_PythonSuli\pycore-220219\photos"

    assert os.path.exists(root_folder), f"Folder: {root_folder} does not exist."
    assert os.path.isdir(root_folder), f"root_folder must be a folder."

    return root_folder


def collect_photos(root_folder):
    photo_files = []
    get_files(
        root_folder=root_folder,
        files=photo_files,
        name_filet=".jpg"
    )

    return photo_files


def create_thumbnail_folder(root_folder):
    thumbnail_folder = os.path.join(root_folder, "_thumbnails")
    if not os.path.exists(thumbnail_folder):
        os.makedirs(thumbnail_folder)

    return thumbnail_folder


def thumbnail_worker(thumbnail_folder):
    while not job_queue.empty():
        file = job_queue.get()
        print(f"thumbnail_worker working on: {file}")

        img = Image.open(file)
        img.thumbnail((THUMBNAIL_SIZE, THUMBNAIL_SIZE))

        new_file_path = os.path.join(thumbnail_folder, os.path.basename(file))
        img.save(new_file_path)

        job_queue.task_done()

main()