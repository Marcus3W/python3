# Abstract classes are classes that contain one or more abstract methods. 
# An abstract method is a method that is declared, but contains no implementation.

# Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.

from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# Write your code below
class Employee(AbstractEmployee):
    def say_id(self):
      print(self.id)

e1 = Employee()
e1.say_id()

