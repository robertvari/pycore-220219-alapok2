from utilities.file_utils import get_files


def get_factorial(n):
    if n < 2:
        return n
    else:
        return n * get_factorial(n-1)

# result = get_factorial(5)
# print(result)


file_list = []
get_files(
    root_folder=r"C:\Work\_PythonSuli\pycore-220219\photos",
    files=file_list,
    name_filet=".xlsx"
)
