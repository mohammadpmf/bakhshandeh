def my_decorator(func):
    def wrapper():
        for i in range(5):
            print(i)
        func()
        for i in range(5, 0, -1):
            print(i)
    return wrapper

def my_decorator2(func):
    def wrapper():
        print('salam')
        func()
        print('malas')
    return wrapper

@my_decorator
# @my_decorator2
def say_whee():
    print("Whee!")

say_whee()
