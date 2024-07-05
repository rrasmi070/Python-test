def sums(func):
    def inner():
        func()
    return inner

def sum_val():
    pass