class Garden(object):

    def __init__(self, diagram, students = ["Alice","Bob","Charlie","David","Eve","Fred","Ginny","Harriet","Ileana","Joseph","Kincaid","Larry"]):
        self.diagram = diagram
        self.students  = sorted(students)
        self.plantCodes = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def plants(self, student):
        index = self.students.index(student) * 2
        return [self.plantCodes[i] for i in [c for row in self.diagram.splitlines() for c in row[index:index+2:]]]
