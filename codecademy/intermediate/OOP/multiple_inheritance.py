# Multiple inheritance in OOP

# In Python, it's possible to inherit from multiple classes. This is called multiple inheritance.

# For example, we have a class called MusicalInstrument that has a method called play:
class MusicalInstrument:
    def play(self):
        print("Playing an instrument.")

# We also have a class called StringInstrument that has a method called bow:
class StringInstrument:
    def bow(self):
        print("Bowing a string instrument.")

# We can create a subclass of both of these classes called Violin that inherits from both MusicalInstrument and StringInstrument:
class Violin(MusicalInstrument, StringInstrument):
    pass

# Now, we can create an instance of Violin and call both methods:

violin = Violin()
violin.play() # Prints "Playing an instrument."
violin.bow() # Prints "Bowing a string instrument."


# ================================ # 

# Another example of multiple inheritance is the following:

class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))

class Cat(Animal):
  pass

class Angry_Cat(Cat):
  pass

my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() # Mr. Cranky says, Hi!

# In this example, the Angry_Cat class inherits from both Cat and Animal. 
# This means that the Angry_Cat class has access to the say_hi method from the Animal class, 
# even though it doesn't inherit from it directly.

# ================================ #


class Animal:
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))

class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))

class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)

my_pet = Hybrid("Fluffy")
my_pet.action() # Fluffy wags tail. Awwww
                # Fluffy bites. OUCH!