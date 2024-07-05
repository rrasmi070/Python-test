# def add(x, y):
#     return x + y

# def calculate(func, x, y):
#     return func(x, y)

# result = calculate(add, 4, 6)
# print(result)  # prints 10

def calculate(func):
    def inner(x,y):
        print("Hiiiiiii")
        y = func(x, y)
        print('Compleet====')
        return y + 5
    return inner
        

@calculate
def add(x,y):
    print('main======')
    return x+y

print(add(3,5))