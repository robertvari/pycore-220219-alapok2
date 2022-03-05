name = "Robert"


def say_hello():
    print(f"Hello {name}")

    def nested_function():
        print(f"Hello {name}, I'm a nested function")

    nested_function()

say_hello()