class School(object):
    def __init__(self, name):
        self.name = name
        self.grades=[[] for i in range(9)]

    def add(self, student, grade):
        self.grades[grade].append(student)

    def grade(self, grade):
        return self.grades[grade]

    def sort(self):
        return [(i, tuple(sorted(g))) for i, g in enumerate(self.grades) if len(g) > 0]
