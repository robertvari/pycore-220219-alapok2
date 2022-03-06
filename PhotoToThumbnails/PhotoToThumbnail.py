import os
from utilities.file_utils import get_files


def main():
    # get root_folder
    root_folder = get_root_folder()

    # collect all photos from root_folder and subfolders
    photo_files = collect_photos(root_folder)


def get_root_folder():
    root_folder = input("Where are your photos?")

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

main()