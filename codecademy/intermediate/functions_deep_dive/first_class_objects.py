# Functions as First Class Objects
# These are the characteristics of first class objects:
#
# A first class object can be stored in a variable
# A first class object can be stored in a data structure (like a list)
# A first class object can be passed as an argument to a function
# A first class object can be returned as the result of a function
#

# Functions as Arguments

def total_bill(func, value):
    total = func(value)
    return total

def add_tip(total):
    return total * 1.2

print(total_bill(add_tip, 100)) # returns 120.0


# Functions as Return Values

def get_math_function(operation):
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    if operation == '+':
        return add
    elif operation == '-':
        return subtract
    
add_function = get_math_function('+')

print(add_function) # returns <function get_math_function.<locals>.add at 0x7f9f1c0b7d30>
print(add_function(2, 3)) # returns 5

subtract_function = get_math_function('-')

print(subtract_function) # returns <function get_math_function.<locals>.subtract at 0x7f9f1c0b7e18>
print(subtract_function(2, 3)) # returns -1


# Nested Functions

def outer_function():
    print('This is outer_function')
    def nested_function():
        print('This is nested_function')
    nested_function()

outer_function() # prints 'This is outer_function' and 'This is nested_function'


# Closures

def outer_function(value):
    def inner_function():
        print(value)
    return inner_function

closure = outer_function('This is a closure')

print(closure) # returns <function outer_function.<locals>.inner_function at 0x7f9f1c0b7d90>

closure() # prints 'This is a closure'


# Decorators

def add_two(number):
    return number + 2

def decorator(func):
    def wrapper(number):
        value = func(number)
        return value * 2
    return wrapper

add_two = decorator(add_two)

print(add_two(10)) # returns 24

# The @ symbol is used to apply a decorator to a function

@decorator
def add_two(number):
    return number + 2

print(add_two(10)) # returns 24


