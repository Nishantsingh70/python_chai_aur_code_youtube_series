import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        for key, value in cache_value.items():
            print(f" key: {key} and value: {value}")
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(2)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(3, 2))
# print(long_running_function(4, 3))

@cache
def long_running_function_2(a, b):
    time.sleep(2)
    return a - b

print(long_running_function_2(2, 3))
print(long_running_function_2(3, 2))
print(long_running_function_2(2, 3))