

class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level
       

class DynamicArray:
    def __init__(self, initial_capacity=5):
        self.capacity = initial_capacity
        self.count = 0
        self.data = [None] * self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity

        for i in range(self.count):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity
        print(f"Array capacity increased to {self.capacity}.")

    def add(self, student):
        if self.count == self.capacity:
            self.resize()

        self.data[self.count] = student
        self.count += 1

    def search(self, student_id):
        for i in range(self.count):
            if self.data[i].student_id == student_id:
                return i
        return -1

    def get(self, index):
        return self.data[index]

    def set(self, index, student):
        self.data[index] = student

    def remove(self, student_id):
        index = self.search(student_id)

        if index == -1:
            return False

        for i in range(index, self.count - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.count - 1] = None
        self.count -= 1
        return True

    def size(self):
        return self.count

    def display(self):
        if self.count == 0:
            print("No student records found.")
            return

        for i in range(self.count):
            s = self.data[i]
            print("--------------------------------")
            print(f"Student ID   : {s.student_id}")
            print(f"Student Name : {s.name}")
            print(f"Course       : {s.course}")
            print(f"Year Level   : {s.year_level}")
        print("--------------------------------")


def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    year_level = input("Enter Year Level: ")

    new_student = Student(student_id, name, course, year_level)
    students.add(new_student)
    print("Student added successfully!")


def display_students(students):
    students.display()


def search_student(students):
    student_id = input("Enter Student ID to search: ")
    index = students.search(student_id)

    if index == -1:
        print("Student not found.")
    else:
        s = students.get(index)
        print("Student Found:")
        print(f"Student ID   : {s.student_id}")
        print(f"Student Name : {s.name}")
        print(f"Course       : {s.course}")
        print(f"Year Level   : {s.year_level}")


def update_student(students):
    student_id = input("Enter Student ID to update: ")
    index = students.search(student_id)

    if index == -1:
        print("Student not found.")
        return

    name = input("Enter new Name: ")
    course = input("Enter new Course: ")
    year_level = input("Enter new Year Level: ")

    updated_student = Student(student_id, name, course, year_level)
    students.set(index, updated_student)
    print("Student updated successfully!")


def remove_student(students):
    student_id = input("Enter Student ID to remove: ")
    success = students.remove(student_id)

    if success:
        print("Student removed successfully!")
    else:
        print("Student not found.")


def display_array_info(students):
    print(f"Number of students: {students.size()}")
    print(f"Current array capacity: {students.capacity}")


def main():
    students = DynamicArray(5)

    while True:
        print("\n================================")
        print(" STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            remove_student(students)
        elif choice == "6":
            display_array_info(students)
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



main()