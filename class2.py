class Student:
    def __init__(self, name, roll_number, division):
        self.name = name
        self.roll_number = roll_number
        self.division = division
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def print_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Division:", self.division)
        print("Marks:")
        for subject, marks in self.marks.items():
            print(subject, ":", marks)
        print("Total Marks:", sum(self.marks.values()))


# Get input from user
name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))
division = input("Enter division: ")

# Create student object
student = Student(name, roll_number, division)

# Get marks for three subjects
subjects = ["Math", "Science", "English"]
for subject in subjects:
    marks = int(input(f"Enter marks for {subject}: "))
    student.add_marks(subject, marks)

# Print student details and total marks
student.print_details()