# Polymophmism: the ability of an object to take on many forms

# Polymorphism with Inheritance

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
employee = Employee()
admin = Admin()
manager = Manager()
meeting = [employee, admin, manager]
for person in meeting:
  person.say_id()
 