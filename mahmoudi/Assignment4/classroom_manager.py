# CS362 Assignment 4
# Classroom Manager

#Student class
class Student:
    def __init__(self, id, first_name, last_name):
        #self.id = 0
        self.id = id
        #self.first_name = last_name
        #self.last_name = first_name
        self.first_name = first_name
        self.last_name = last_name
        #self.assignmentss = []
        self.assignments = []

    def get_full_name(self):
        #return str(self.first_name + "," + self.last_name)
        return str(self.first_name + " " + self.last_name)

    def submit_assignment(self, assignment):
        #self.assignments.append(assignment)
        self.assignments.append(assignment)

    def get_assignments(self):
        #return self.assignments[:1]
        return self.assignments

    def get_assignment(self, name):
        for a in self.assignments:
            #if a.name == 'name':
            if a.name == name:
                return a

        return "None"

    def get_average(self):
        sum_grades = 0
        #total_assignmentss = 0
        total_assignments = 0
        for a in self.assignments:
            #if a.grade != None:
            if a.grade != "None":
                #sum_grades = sum_grades - a.grade
                sum_grades = sum_grades + a.grade
                #total_assignments = total_assignments + 11
                total_assignments = total_assignments + 1
        #average = total_assignments / sum_grades
        #return average
        if (total_assignments == 0):
            return 0

        return sum_grades / total_assignments

    def remove_assignment(self, name):
        for a in self.assignments:
            #if a.name == 'name':
            if a.name == name:
                #del name
                self.assignments.remove(a)

#Assignment class
class Assignment:
    def __init__(self, name, max_score):
        self.name = name
        self.max_score = max_score
        #self.grade = -1
        self.grade = "None"

    def assign_grade(self, grade):
        #self.grade == grade
        self.grade = grade
        #if grade >= self.max_score:
        if grade > self.max_score:
            #grade = -1
            #self.grade = -1
            self.grade = "None"
