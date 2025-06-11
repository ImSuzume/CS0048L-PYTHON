class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # {subject: [score1, score2, ...]}

    def add_grade(self, subject, score):
        if 0 <= score <= 100:
            if subject in self.grades:
                self.grades[subject].append(score)
            else:
                self.grades[subject] = [score]
            print(f"Added score {score} for {self.name} in {subject}.")
        else:
            print("Score must be between 0 and 100.")

    def calculate_averages(self):
        if not self.grades:
            print(f"No grades recorded for {self.name}.")
        else:
            print(f"\nAverages for {self.name}:")
            for subject, scores in self.grades.items():
                avg = sum(scores) / len(scores)
                print(f"{subject.capitalize()}: {avg:.2f}")


class GradeTracker:
    def __init__(self):
        self.students = {}  # {student_name: Student instance}

    def add_student(self):
        name = input("Enter student name: ").strip()
        if name in self.students:
            print("Student already exists.")
        else:
            self.students[name] = Student(name)
            print(f"Student '{name}' added.")

    def add_grade(self):
        name = input("Enter student name: ").strip()
        if name not in self.students:
            print("Student not found. Please add the student first.")
            return
        subject = input("Enter subject: ").strip().lower()
        score_input = input("Enter score (0-100): ").strip()

        if score_input.replace('.', '', 1).isdigit():
            score = float(score_input)
            self.students[name].add_grade(subject, score)
        else:
            print("Invalid score input.")

    def view_grades(self):
        if not self.students:
            print("No students available.")
            return
        for student in self.students.values():
            print(f"\nGrades for {student.name}:")
            if not student.grades:
                print("  No grades recorded.")
            else:
                for subject, scores in student.grades.items():
                    print(f"  {subject.capitalize()}: {scores}")

    def calculate_averages(self):
        if not self.students:
            print("No students to calculate averages for.")
            return
        for student in self.students.values():
            student.calculate_averages()

    def menu(self):
        while True:
            print("\n===== Student Grade Tracker =====")
            print("1. Add Student")
            print("2. Add Grade")
            print("3. View All Grades")
            print("4. Calculate Averages")
            print("5. Exit")
            choice = input("Choose an option (1-5): ").strip()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_grade()
            elif choice == '3':
                self.view_grades()
            elif choice == '4':
                self.calculate_averages()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select from 1 to 5.")


# Run the program
tracker = GradeTracker()
tracker.menu()