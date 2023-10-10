# Checkpoint 2
from roster import student_roster
import itertools

class Classroom_organiser:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    if self.index >= len(self.sorted_names):
      raise StopIteration
    count = self.index
    self.index += 1
    return count
  
  def get_tuples(self):
    print(list(itertools.combinations(self.sorted_names, 2)))

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students