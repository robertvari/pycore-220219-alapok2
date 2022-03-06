add_number = lambda a, b: a+b
multiply_number = lambda a, b: a*b
divide_number = lambda a, b: a/b

# print(add_number(10, 5))
# print(multiply_number(10, 5))
# print(divide_number(10, 5))

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]
number_list = [3, 1, -20, 345, 7]


print(sorted(name_list, key=lambda name: name.split()[-1]))