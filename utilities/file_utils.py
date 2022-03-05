import os


def get_files(root_folder: str) -> list:
    """
    This functions takes a string as a folder path and returns a list of files (str)
    :param root_folder: path like string
    :return: List of files list[str]
    """

    assert os.path.exists(root_folder), f"Folder: {root_folder} does not exist."
    assert os.path.isdir(root_folder), f"root_folder must be a folder."

    # list comprehension
    result = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]

    return result