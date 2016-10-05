class Student(Person):
   
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        avg = sum(scores) / len(scores)
        if avg >= 90:
            return "O"
        if avg >= 80:
            return "E"
        if avg >= 70:
            return "A"
        if avg >= 55:
            return "P"
        if avg >= 40:
            return "D"
        return "T"