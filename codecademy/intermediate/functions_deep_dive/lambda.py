# A lambda function (also commonly called an anonymous function) is a one-line shorthand for function

# Non-lambda example
def add_two(input):
    return input + 2

# Lambda alternative
add_two_lambda = lambda input: input + 2

print(add_two(10)) # returns 12
print(add_two_lambda(10)) # returns 12 


## Additonal examples

# Non-lambda example
def print_full_name(first_name, last_name):
    return f'Your full name is {first_name} {last_name}'

# Lambda alternative
full_name_lambda = lambda first_name, last_name: f'Your full name is {first_name} {last_name}'

print(print_full_name('John', 'Doe')) # returns 'Your full name is John Doe'
print(full_name_lambda('John', 'Doe')) # returns 'Your full name is John Doe'



# Non-lambda example
def add_random_number():
    import random
    return random.randint(1, 10)

# Lambda alternative
import random
add_random_number_lambda = lambda: random.randint(1, 10)

print(add_random_number()) # returns a random number between 1 and 10
print(add_random_number_lambda()) # returns a random number between 1 and 10

