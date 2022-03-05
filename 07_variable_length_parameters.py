# variable length arguments
def print_my_data(*args):
    for i in args:
        print(i)

# print_my_data("Robert", 32, "robert@gmail.com")

# variable length keyword arguments
def print_my_data2(**kwargs):
    print(kwargs)


def print_my_data3(*args, **kwargs):
    print(kwargs)


print_my_data2(
    name="Robert",
    age=32,
    email="robert@gmail.com"
)