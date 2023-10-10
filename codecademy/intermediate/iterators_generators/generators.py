# Generators are a type of iterable, like lists or tuples.

# Basic example of a generator function

def my_range(x):
  i = 0
  while i < x:
    yield i
    i += 1
    
for x in my_range(5):
    print(x)


# ============================== #

# Use of next() to iterate through a generator function

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

# Create a generator object
nums = my_range(5)

# Iterate through the generator object using next()
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


# ============================== #

# Generator Expressions

def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Checkpoint 1
cs_courses = cs_generator()
for course in cs_courses:
  print(course)

# Checkpoint 2
cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5))

# Checkpoint 3
for course in cs_generator_exp:
  print(course)


# ============================== #

# Generator Methods

# .send() method
def generator():
  count = 0
  while True:
    n = yield count
    if n is not None:
      count = n
    count += 1

my_generator = generator()
print(next(my_generator)) # Output: 0
print(next(my_generator)) # Output: 1
print(my_generator.send(3)) # Output: 4
print(next(my_generator)) # Output: 5

# .throw() method
def generator():
  try:
    yield "Hello"
  except Exception:
    yield "Caught an exception"

my_generator = generator()
print(next(my_generator)) # Output: Hello
# print(my_generator.throw(Exception, "Caught an exception")) # Output: Caught an exception

# .close() method
def generator():
  i = 0
  while True:
    try:
      yield i
    except GeneratorExit:
      print("Early exit, BYE!")
      break
    i += 1

my_generator = generator()
for item in my_generator:
  print(item)
  if item == 1:
    my_generator.close()


# ============================== #

# Connecitng Generators

def cs_courses():
    yield 'Computer Science'
    yield 'Artificial Intelligence'

def art_courses():
    yield 'Intro to Art'
    yield 'Selecting Mediums'


def all_courses():
    yield from cs_courses()
    yield from art_courses()

combined_generator = all_courses()

print(next(combined_generator))
print(next(combined_generator))
print(next(combined_generator))
print(next(combined_generator))


# ============================== #

# Generator Pipelines (Nested Generators)

## Generator pipelines allow us to use multiple generators to perform
## a series of operations all within one expression.

def course_generator():
    yield ("Computer Science", 5)
    # Write your code below:
    yield ("Art", 10)
    yield ("Business", 15)

def add_five_students(courses):
    for course, num_students in courses:
      yield (course, num_students + 5)

increased_courses = add_five_students(course_generator())
for course in increased_courses:
  print(course)


# ============================== #

# Review


def summa():
    yield 'Summa Cum Laude'

def magna():
    yield 'Magna Cum Laude' 

def cum_laude():
    yield 'Cum Laude'

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()


def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1


days = 25
countdown_generator = (day for day in range(days, -1,-1))
grad_days = graduation_countdown(days)
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print("Days Left: " + str(day))


days = 25
gpas = [3.2, 4.0, 3.6, 2.9]
honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)