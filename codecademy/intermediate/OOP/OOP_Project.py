# School Catalogue

class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    
    def __repr__(self):
        return "A {} school with {} students".format(self.level, self.numberOfStudents)
    
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level
    
    def get_number_of_students(self):
        return self.numberOfStudents
    
    def set_number_of_students(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy
    
    def __repr__(self):
        return "A {} school with {} students".format(self.name, self.numberOfStudents)
    
    def get_pickup_policy(self):
        return self.pickupPolicy


class MiddleSchool(School):
    def __init__(self, name, numberOfStudents):
        super().__init__(name, "middle", numberOfStudents)
        self.name = name
    
    def __repr__(self):
        return "A {} school with {} students".format(self.name, self.numberOfStudents)
    
class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeam):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeam = sportsTeam

    def get_sports_teams(self):
        return self.sportsTeam



a = School("Codecademy", "high", 100)
print(a)
print(a.get_name())
print(a.get_level())
a.set_number_of_students(200)
print(a.get_number_of_students())

b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickup_policy())
print(b)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sports_teams())
print(c)