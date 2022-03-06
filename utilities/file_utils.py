import os


def get_files(root_folder: str, files: list, name_filet=None) -> list:
    """
    This functions takes a string as a folder path and returns a list of files (str)
    :param root_folder: path like string
    :param name_filet: Optional filter on files
    :param files: Empty list for storing files
    :return: List of files list[str]
    """

    assert os.path.exists(root_folder), f"Folder: {root_folder} does not exist."
    assert os.path.isdir(root_folder), f"root_folder must be a folder."

    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]

    # get all files in current root_folder
    for i in folder_content:
        if os.path.isfile(i):
            if name_filet:
                if name_filet.lower() in i.lower():
                    files.append(i)
            else:
                files.append(i)

    # find all folders in folder_content
    subfolders = []
    for i in folder_content:
        if os.path.isdir(i):
            subfolders.append(i)

    for folder in subfolders:
        get_files(folder, files)