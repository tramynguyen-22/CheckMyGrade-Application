#Name: Tramy Nguyen
#LAB 1 - DATA 200

import csv
import base64
import random
import time
import statistics

# -------------------------
# Student Class
# -------------------------
class Student:

    def __init__(self, first_name, last_name, email_address, course_id, grade, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_id = course_id
        self.grade = grade
        self.marks = float(marks)

    def display_records(self):
        print(self.first_name, self.last_name, self.email_address,
              self.course_id, self.grade, self.marks)

    def add_new_student(self):
        print("Student added:", self.email_address)

    def delete_new_student(self):
        print("Student deleted:", self.email_address)

    def check_my_grades(self):
        print("Grade:", self.grade)

    def update_student_record(self, grade=None, marks=None):

        if grade:
            self.grade = grade

        if marks:
            self.marks = float(marks)

        print("Student updated")

    def check_my_marks(self):
        print("Marks:", self.marks)


# -------------------------
# Course Class
# -------------------------
class Course:

    def __init__(self, course_id, credits, course_name):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name

    def display_courses(self):
        print(self.course_id, self.credits, self.course_name)

    def add_new_course(self):
        print("Course added:", self.course_id)

    def delete_new_course(self):
        print("Course deleted:", self.course_id)


# -------------------------
# Professor Class
# -------------------------
class Professor:

    def __init__(self, name, email_address, rank, course_id):
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id

    def professors_details(self):
        print(self.name, self.email_address, self.rank, self.course_id)

    def add_new_professor(self):
        print("Professor added:", self.email_address)

    def delete_professore(self):
        print("Professor deleted:", self.email_address)

    def modify_professor_details(self, name=None, rank=None):

        if name:
            self.name = name

        if rank:
            self.rank = rank

        print("Professor updated")

    def show_course_details_by_professor(self):
        print(self.name, "teaches course", self.course_id)


# -------------------------
# Grades Class
# -------------------------
class Grades:

    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def display_grade_report(self):
        print(self.grade_id, self.grade, self.marks_range)

    def add_grade(self):
        print("Grade added:", self.grade)

    def delete_grade(self):
        print("Grade deleted:", self.grade)

    def modify_grade(self, grade=None, marks_range=None):

        if grade:
            self.grade = grade

        if marks_range:
            self.marks_range = marks_range

        print("Grade updated")


# -------------------------
# LoginUser Class
# -------------------------
class LoginUser:

    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password

    def Login(self, entered_password):

        if entered_password == self.password:
            print("Login successful")
        else:
            print("Login failed")

    def Logout(self):
        print("Logged out:", self.email_id)

    def Change_password(self, new_password):
        self.password = new_password
        print("Password changed")

    def Encrypt_password(self):

        encoded = base64.b64encode(self.password.encode()).decode()

        return encoded

    def decrypt_password(self, encrypted_password):

        decoded = base64.b64decode(encrypted_password.encode()).decode()

        return decoded

def load_students():
    students = []

    with open("Student.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = Student(
                row["First_name"],
                row["Last_name"],
                row["Email_address"],
                row["Course_id"],
                row["Grades"],
                row["Marks"]
            )
            students.append(student)

    return students

def add_student(first_name, last_name, email, course_id, grade, marks):

    with open("Student.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([email, first_name, last_name, course_id, grade, marks])

    print("Student added successfully")

def search_student(email):
    students = load_students()

    for student in students:
        if student.email_address == email:
            print("Student found:")
            student.display_records()
            return student

    print("Student not found")
    return None

def timed_search_student(email):
    start_time = time.perf_counter()

    search_student(email)

    end_time = time.perf_counter()

    print("Search time:", end_time - start_time, "seconds")


def sort_students_by_marks():
    students = load_students()

    students.sort(key=lambda student: student.marks)

    print("Students sorted by marks:")

    for student in students:
        student.display_records()

    return students

def timed_sort_students_by_marks():
    start_time = time.perf_counter()

    sort_students_by_marks()

    end_time = time.perf_counter()

    print("Sort by marks time:", end_time - start_time, "seconds")


def add_course(course_id, course_name, description):
    with open("Course.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([course_id, course_name, description])

    print("Course added successfully")

def add_login_user(user_id, password, role):
    user = LoginUser(user_id, password)
    encrypted_password = user.Encrypt_password()

    with open("Login.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, encrypted_password, role])

    print("Login user added successfully")

def test_login(user_id, entered_password):
    with open("Login.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["User_id"] == user_id:
                user = LoginUser(user_id, "")
                decrypted_password = user.decrypt_password(row["Password"])

                if entered_password == decrypted_password:
                    print("Login successful")
                else:
                    print("Login failed")
                return

    print("User not found")

def add_professor(professor_id, professor_name, rank, course_id):
    with open("Professor.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([professor_id, professor_name, rank, course_id])

    print("Professor added successfully")

def show_course_by_professor(professor_id):
    with open("Professor.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Professor_id"] == professor_id:
                print("Professor found:")
                print("Professor Name:", row["Professor_Name"])
                print("Course ID:", row["Course_id"])
                return

    print("Professor not found")

def modify_professor(professor_id, new_name=None, new_rank=None, new_course_id=None):
    with open("Professor.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        professors = list(reader)

    with open("Professor.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Professor_id", "Professor_Name", "Rank", "Course_id"])

        found = False

        for row in professors:
            if row["Professor_id"] == professor_id:
                found = True

                if new_name is not None:
                    row["Professor_Name"] = new_name
                if new_rank is not None:
                    row["Rank"] = new_rank
                if new_course_id is not None:
                    row["Course_id"] = new_course_id

            writer.writerow([
                row["Professor_id"],
                row["Professor_Name"],
                row["Rank"],
                row["Course_id"]
            ])

    if found:
        print("Professor record updated successfully")
    else:
        print("Professor not found")

def delete_professor(professor_id):
    with open("Professor.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        professors = list(reader)

    with open("Professor.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Professor_id", "Professor_Name", "Rank", "Course_id"])

        found = False

        for row in professors:
            if row["Professor_id"] == professor_id:
                found = True
                continue

            writer.writerow([
                row["Professor_id"],
                row["Professor_Name"],
                row["Rank"],
                row["Course_id"]
            ])

    if found:
        print("Professor record deleted successfully")
    else:
        print("Professor not found")

def delete_course(course_id):
    with open("Course.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        courses = list(reader)

    with open("Course.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Course_id", "Course_name", "Description"])

        found = False

        for row in courses:
            if row["Course_id"] == course_id:
                found = True
                continue

            writer.writerow([
                row["Course_id"],
                row["Course_name"],
                row["Description"]
            ])

    if found:
        print("Course deleted successfully")
    else:
        print("Course not found") 

def modify_course(course_id, new_course_name=None, new_description=None):
    with open("Course.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        courses = list(reader)

    with open("Course.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Course_id", "Course_name", "Description"])

        found = False

        for row in courses:
            if row["Course_id"] == course_id:
                found = True

                if new_course_name is not None:
                    row["Course_name"] = new_course_name

                if new_description is not None:
                    row["Description"] = new_description

            writer.writerow([
                row["Course_id"],
                row["Course_name"],
                row["Description"]
            ])

    if found:
        print("Course updated successfully")
    else:
        print("Course not found")

def update_student(email, new_grade, new_marks):
    students = load_students()

    with open("Student.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email_address", "First_name", "Last_name", "Course_id", "Grades", "Marks"])

        found = False

        for student in students:
            if student.email_address == email:
                student.grade = new_grade
                student.marks = float(new_marks)
                found = True

            writer.writerow([
                student.email_address,
                student.first_name,
                student.last_name,
                student.course_id,
                student.grade,
                student.marks
            ])

    if found:
        print("Student record updated successfully")
    else:
        print("Student not found")

def delete_student(email):
    students = load_students()

    with open("Student.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email_address", "First_name", "Last_name", "Course_id", "Grades", "Marks"])

        found = False

        for student in students:
            if student.email_address == email:
                found = True
                continue

            writer.writerow([
                student.email_address,
                student.first_name,
                student.last_name,
                student.course_id,
                student.grade,
                student.marks
            ])

    if found:
        print("Student deleted successfully")
    else:
        print("Student not found")

def sort_students_by_email():
    students = load_students()

    students.sort(key=lambda student: student.email_address.lower())

    print("Students sorted by email:")

    for student in students:
        student.display_records()

    return students

def timed_sort_students_by_email():
    start_time = time.perf_counter()

    sort_students_by_email()

    end_time = time.perf_counter()

    print("Sort by email time:", end_time - start_time, "seconds")

def generate_students(n):

    first_names = ["Alex","Bella","Chris","Diana","Eric","Fiona","George","Hannah","Ivan","Julia"]
    last_names = ["Lee","Tran","Nguyen","Smith","Brown","Garcia","Lopez","Wilson","Anderson","Clark"]

    with open("Student.csv", "a", newline="") as file:
        writer = csv.writer(file)

        for i in range(n):

            first = random.choice(first_names)
            last = random.choice(last_names)

            email = f"{first.lower()}.{last.lower()}{i}@sjsu.edu"

            course_id = "DATA200"

            marks = random.randint(60,100)

            if marks >= 93:
                grade = "A"
            elif marks >= 90:
                grade = "A-"
            elif marks >= 87:
                grade = "B+"
            elif marks >= 83:
                grade = "B"
            elif marks >= 80:
                grade = "B-"
            elif marks >= 77:
                grade = "C+"
            elif marks >= 73:
                grade = "C"
            elif marks >= 70:
                grade = "C-"
            elif marks >= 67:
                grade = "D+"
            elif marks >= 63:
                grade = "D"
            elif marks >= 60:
                grade = "D-"
            else:
                grade = "F"

            writer.writerow([email, first, last, course_id, grade, marks])

    print(n, "students generated with matching grades")

def load_courses():
    courses = []

    with open("Course.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            course = Course(
                row["Course_id"],
                3,
                row["Course_name"]
            )
            courses.append(course)

    return courses


def load_professors():
    professors = []

    with open("Professor.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            professor = Professor(
                row["Professor_Name"],
                row["Professor_id"],
                row["Rank"],
                row["Course_id"]
            )
            professors.append(professor)

    return professors


def load_login_users():
    users = []

    with open("Login.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            user = LoginUser(
                row["User_id"],
                row["Password"]
            )
            users.append(user)

    return users


if __name__ == "__main__":
    
   #add_student("Tramy","Nguyen","tramy.nguyen@sjsu.edu","DATA200","A",95)
   #add_student("Alex","Lee","alex.lee@sjsu.edu","DATA200","B",88)
   #add_student("Bella","Tran","bella.tran@sjsu.edu","DATA200","A-",91)

  #students = load_students()
  
  #print("Students loaded:", len(students))

   #search_student("tramy.nguyen@sjsu.edu")
   #sort_students_by_marks()

   #add_course("DATA200", "Data Science", "Provides insight about DS and Python")
   #add_login_user("tramy.nguyen@sjsu.edu", "Welcome12#_", "student")

   #test_login("tramy.nguyen@sjsu.edu", "Welcome12#_")

   #add_professor("paramdeep.saini@sjsu.edu","Paramdeep Saini", "Senior Professor", "DATA200")
   #update_student("tramy.nguyen@sjsu.edu", "A+", 98)
   #delete_student("tramy.nguyen@sjsu.edu")
   #sort_students_by_email()

   #show_course_by_professor("paramdeep.saini@sjsu.edu")
   #modify_professor("paramdeep.saini@sjsu.edu", "Paramdeep Saini", "Associate Professor", "DATA200")
   #delete_professor("paramdeep.saini@sjsu.edu")
   #delete_course("DATA200")

   #generate_students(1000) 
  #timed_search_student("bella.brown0@sjsu.edu")
  #timed_sort_students_by_marks()
  #timed_sort_students_by_email()

   #add_course("DATA300", "Machine Learning", "Intro to ML")
   #modify_course("DATA300", "Machine Learning", "Updated ML course description")
   # delete_course("DATA300")

   #add_professor("john.doe@sjsu.edu", "John Doe", "Professor", "MATH 111")
   #add_professor("sarah.lee@sjsu.edu", "Sarah Lee", "Associate Professor", "ENGR 100")

   #modify_professor("john.doe@sjsu.edu", "John Doe", "Senior Professor", "MATH 111")
   #delete_professor("john.doe@sjsu.edu")
