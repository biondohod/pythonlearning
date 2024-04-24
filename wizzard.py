class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard): 
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the dark arts")
wizard = Wizard("Albus")

