import time, json


def timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(f"Process time: {time.time()-start_time}")

        with open("timer_data.txt", "a") as f:
            f.write(f"\nProcess time: {time.time()-start_time}")

        return result
    return wrapper


def useless_decorator(function):
    def wrapper(*args, **kwargs):
        print("Hello. I'm the useless_decorator")
        function(*args, **kwargs)
    return wrapper