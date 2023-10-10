from roster import student_roster
from classroom_organiser import Classroom_organiser
import itertools

# Checkpoint 1
student_roster_iterator = iter(student_roster)

for student in student_roster_iterator:
    print(next(student_roster_iterator))

# Checkpoint 3
classroom = Classroom_organiser()

# for student in classroom:
#     print(next(student))

# Checkpoint 4
classroom.get_tuples()

# Checkpoint 5
students_of_math = classroom.get_students_with_subject('Math')
students_of_science = classroom.get_students_with_subject('Science')
combined_subjects = itertools.chain(students_of_math, students_of_science)

total = itertools.combinations(combined_subjects, 4)
print(list(total))

x = float(2.8)
print(x)

print(type(x))

y = "Hello"[0]
print(y)

