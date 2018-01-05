students = ["Alice","Bob","Charlie","David","Eve","Fred","Ginny","Harriet","Ileana","Joseph","Kincaid","Larry"]
plants = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

class Garden(object):
    def __init__(self, diagram, students=students):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student) * 2
        return [plants[i] for i in [c for row in self.diagram.splitlines() for c in row[index:index+2:]]]
