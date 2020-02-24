from unittest import TestCase
import classroom_manager

class TestStudent(TestCase):
    def testinit(self):
        # Initialize test data
        id = 1
        first_name = "Alpha"
        last_name = "Omega"

        # Instantiate Student object
        student = classroom_manager.Student(id, first_name, last_name)

        # Verify that the class variables have the expected values
        self.assertEqual(id, student.id)                                            # This failed at first, id was always set to 0
        self.assertEqual(first_name, student.first_name)                            # This failed at first, first_name was always set to last_name
        self.assertEqual(last_name, student.last_name)                              # This failed at first, last_name was always set to first_name
        self.assertEqual(0, len(student.assignments))                               # This failed at first, there was a typo on "assignmentss"

    def test_get_full_name(self):
        # Initialize test data
        id = 1
        first_name = "Alpha"
        last_name = "Omega"

        # Instantiate Student object
        student = classroom_manager.Student(id, first_name, last_name)

        # Verify that the class variables have the expected values
        self.assertEqual(first_name + " " + last_name, student.get_full_name())     # This failed at first, get_full_name() always returned first_name,last_name

    def test_submit_assignment(self):
        # Initialize test data
        id = 1
        first_name = "Alpha"
        last_name = "Omega"
        assignment_name = "Homework 1"
        assignment_max = 100

        # Instantiate Student and Assignment objects
        student = classroom_manager.Student(id, first_name, last_name)
        assignment = classroom_manager.Assignment(assignment_name, assignment_max)

        # Call submit_assignment
        student.submit_assignment(assignment)

        # Verify that the class variables have the expected values
        self.assertEqual(1, len(student.assignments))                               # This failed at first, assignment was appended twice to assignments
        self.assertEqual(assignment, student.assignments[0])

    def test_get_assignments(self):
        # Initialize test data
        id = 1
        first_name = "Alpha"
        last_name = "Omega"
        assignment1_name = "Homework 1"
        assignment1_max = 100
        assignment2_name = "Homework 2"
        assignment2_max = 50
        assignment3_name = "Homework 3"
        assignment3_max = 25
        assignments = []

        # Instantiate Student object
        student = classroom_manager.Student(id, first_name, last_name)

        # Call submit_assignment
        assignments.append(classroom_manager.Assignment(assignment1_name, assignment1_max))
        assignments.append(classroom_manager.Assignment(assignment2_name, assignment2_max))
        assignments.append(classroom_manager.Assignment(assignment3_name, assignment3_max))
        student.submit_assignment(assignments[0])
        student.submit_assignment(assignments[1])
        student.submit_assignment(assignments[2])

        # Verify that the class variables have the expected values
        self.assertEqual(assignments, student.get_assignments())                    # This failed at first, get_assignments wasn't returning the right number of elements

    def test_get_assignment(self):
        # Initialize test data
        id = 1
        first_name = "Alpha"
        last_name = "Omega"
        assignment1_name = "Homework 1"
        assignment1_max = 100
        assignment2_name = "Homework 2"
        assignment2_max = 50
        assignment3_name = "Homework 3"
        assignment3_max = 25
        assignments = []

        # Instantiate Student object
        student = classroom_manager.Student(id, first_name, last_name)

        # Call submit_assignment
        assignments.append(classroom_manager.Assignment(assignment1_name, assignment1_max))
        assignments.append(classroom_manager.Assignment(assignment2_name, assignment2_max))
        assignments.append(classroom_manager.Assignment(assignment3_name, assignment3_max))
        student.submit_assignment(assignments[0])
        student.submit_assignment(assignments[1])

        # Verify that the class variables have the expected values
        self.assertEqual(assignments[0], student.get_assignment(assignment1_name))  # This failed at first, get_assignment() would only look for assignments with the name "name"
        self.assertEqual(assignments[1], student.get_assignment(assignment2_name))
        self.assertEqual("None", student.get_assignment(assignment3_name))          # This failed at first, get_assignment didn't return anything if assignment didn't exist

    def test_get_average(self):
        # Initialize test data
        id = 1
        first_name = "Alpha"
        last_name = "Omega"
        assignment1_name = "None"
        assignment1_max = 100
        assignment2_name = "Zero"
        assignment2_max = 50
        assignment3_name = "Grade"
        assignment3_max = 25
        assignment3_grade = 20
        assignments = []

        # Instantiate Student object
        student = classroom_manager.Student(id, first_name, last_name)

        # Initialize assignments
        assignments.append(classroom_manager.Assignment(assignment1_name, assignment1_max))
        assignments.append(classroom_manager.Assignment(assignment2_name, assignment2_max))
        assignments.append(classroom_manager.Assignment(assignment3_name, assignment3_max))
        assignments[0].assign_grade(assignment1_max + 1)
        assignments[1].assign_grade(0)
        assignments[2].assign_grade(assignment3_grade)

        # Verify that the class variables have the expected values
        student.submit_assignment(assignments[0])
        self.assertEqual(0, student.get_average())                                  # This failed at first: typo in "total_assignmentss", None should be "None" (divide by zero error), and sum_grades, total_assignments, and average are all not calculated right

        student.submit_assignment(assignments[1])
        self.assertEqual(0, student.get_average())

        student.submit_assignment(assignments[2])
        self.assertEqual(assignment3_grade / 2, student.get_average())

    def test_remove_assignment(self):
        # Initialize test data
        id = 1
        first_name = "Alpha"
        last_name = "Omega"
        assignment1_name = "Homework 1"
        assignment1_max = 100
        assignment2_name = "Homework 2"
        assignment2_max = 50
        assignment3_name = "Homework 3"
        assignment3_max = 25
        assignments = []

        # Instantiate Student object
        student = classroom_manager.Student(id, first_name, last_name)

        # Initialize assignments
        assignments.append(classroom_manager.Assignment(assignment1_name, assignment1_max))
        assignments.append(classroom_manager.Assignment(assignment2_name, assignment2_max))
        assignments.append(classroom_manager.Assignment(assignment3_name, assignment3_max))
        student.submit_assignment(assignments[0])
        student.submit_assignment(assignments[1])
        student.submit_assignment(assignments[2])

        # Verify that the class variables have the expected values
        student.remove_assignment(assignment1_name + assignment2_name + assignment3_name)   # Ensures that this will not be an existing name (unless they're all empy strings)
        self.assertEqual(3, len(student.assignments))                               # This failed at first, remove_assignment was always looking for "name" instead of using name, and the remove part was wrong
        self.assertEqual(assignments[0], student.assignments[0])
        self.assertEqual(assignments[1], student.assignments[1])
        self.assertEqual(assignments[2], student.assignments[2])

        student.remove_assignment(assignment2_name)
        self.assertEqual(2, len(student.assignments))
        self.assertEqual(assignments[0], student.assignments[0])
        self.assertEqual(assignments[2], student.assignments[1])

        student.remove_assignment(assignment1_name)
        self.assertEqual(1, len(student.assignments))
        self.assertEqual(assignments[2], student.assignments[0])

        student.remove_assignment(assignment3_name)
        self.assertEqual(0, len(student.assignments))


class TestAssignment(TestCase):
    def test_init(self):
        # Initialize test data
        name = "Homework"
        max_score = 100

        # Instantiate Student object
        assignment = classroom_manager.Assignment(name, max_score)

        # Verify that the class variables have the expected values
        self.assertEqual(name, assignment.name)
        self.assertEqual(max_score, assignment.max_score)
        self.assertEqual("None", assignment.grade)                                  # This failed at first, grade was always set to -1

    def test_assign_grade(self):
        # Initialize test data
        name = "Homework"
        max_score = 100
        grade_lower = max_score - 1
        grade_equal = max_score
        grade_higher = max_score + 1

        # Instantiate Student object
        assignment = classroom_manager.Assignment(name, max_score)

        # Verify that the class variables have the expected values
        assignment.assign_grade(grade_lower)
        self.assertEqual(grade_lower, assignment.grade)                             # This failed at first, grade was never set to anything

        assignment.assign_grade(grade_higher)
        self.assertEqual("None", assignment.grade)                                  # This failed at first, grade was never set to anything, and when it was fixed it would return -1

        assignment.assign_grade(grade_equal)
        self.assertEqual(grade_equal, assignment.grade)                             # This failed at first, grade would return as "None" if it was equal to max_score
