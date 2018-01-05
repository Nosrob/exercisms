class Garden(object):
    studentsList = ["Alice","Bob","Charlie","David","Eve","Fred","Ginny","Harriet","Ileana","Joseph","Kincaid","Larry"]
    plantCodes = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
    
    def __init__(self, diagram, students = studentsList):
        self.diagram = diagram
        self.students  = sorted(students)

    def plants(self, student):
        index = self.students.index(student) * 2
        return [self.plantCodes[i] for i in [c for row in self.diagram.splitlines() for c in row[index:index+2:]]]
