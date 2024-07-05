def decorator1(func):
    def wrapper():
        print("Decorator 1 - Before function")
        res =func()
        # print("Decorator 1 - After function", res)
        print(res)
        return res * res
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 - Before function")
        z = func()
        print("Decorator 2 - After function")
        print(z)
        return z * 2
    return wrapper

def decorator3(func):
    def wrapper():
        print("Decorator 3 - Before function")
        z = func()
        print(z)
        print("Decorator 3 - After function")
        return 3 * z
    return wrapper

@decorator1
@decorator2
@decorator3
def my_function():
    # print("Inside my_function-0",x+y)
    return 10

print(my_function())
