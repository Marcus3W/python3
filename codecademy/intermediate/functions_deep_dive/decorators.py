# Decorators

## Decorating a function with a decorator

# def title_decorator(print_name_function):
#     def wrapper():
#         print('Mr:')
#         print_name_function()
#     return wrapper

# def print_my_name():
#     print('Bob')

# decorated_function = title_decorator(print_my_name)

# decorated_function()

## Decorators

# def title_decorator(print_name_function):
#     def wrapper():
#         print('Mr:')
#         print_name_function()
#     return wrapper

# @title_decorator
# def print_my_name():
#     print('Bob')

# print_my_name()


## Decorattors with Parameters

def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print('Mr:')
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_my_name(name, age):
    print(name + " you are " + str(age))

print_my_name('Steve', 36)