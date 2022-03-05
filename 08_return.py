def add_numbers(a, b):
    return a+b


def multiply_numbers(a, b):
    return a*b


def divide_numbers(a, b):
    return a / b


add_result = add_numbers(2, 10)
multiply_result = multiply_numbers(add_result, 2)
divide_result = divide_numbers(multiply_result, 100)

print(divide_result)