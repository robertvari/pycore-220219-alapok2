def timer(function):
    def wrapper():
        function()
    return wrapper