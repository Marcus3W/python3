# Built-in Higher-Order Functions

# There are several built-in higher-order functions in Python. We’ll explore three of them in this lesson:

#     map()
#     filter()
#     reduce()

# Map

# The map() function takes two arguments:

#     A function
#     An iterable

# map() applies the function argument to each item in the iterable. Below are a few examples:

# Example
numbers = [1, 2, 3, 4, 5]

double = lambda num: num * 2

result = map(double, numbers)
print(list(result)) # returns <map object at 0x7f9f1c0b7f28>


# Filter

# The filter() function takes two arguments:

#    A function that returns True or False
#    An iterable

# filter() applies the function argument to each item in the iterable and returns a new iterable containing only the items for which the function argument returns True. Below are a few examples:

# Example
names = ['Karen', 'Jim', 'Kim']

k_names = filter(lambda name: name[0] == 'K', names)

print(list(k_names)) # returns ['Karen', 'Kim']


# Reduce

# The reduce() function takes two arguments:

#     A function that takes two arguments
#     An iterable

# reduce() applies the function argument to the first two items in the iterable, then applies the function to the result of the first two items and the third item in the iterable, and so on, until all of the items in the iterable are used. The return value is a single value. Below are a few examples:

# Example

from functools import reduce

int_list = [3, 6, 9, 12]

reduce_int_list = reduce(lambda num1, num2: num1 * num2, int_list)

print(reduce_int_list) # returns 1944
# This process was essentially the same as multiplying 3*6*9*12.



