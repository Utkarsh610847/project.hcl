
# ==========================================
# STUDENT MANAGEMENT SYSTEM
# Using Core Python
# ==========================================

students = []


# FUNCTION 1: Add Student

def add_student():

    print("\n----- ADD STUDENT -----")

    roll = input("Enter Roll Number: ")

    # Check duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Roll Number already exists!")
            return

    name = input("Enter Student Name: ")

    marks1 = float(input("Enter Python Marks: "))
    marks2 = float(input("Enter Maths Marks: "))
    marks3 = float(input("Enter English Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "python": marks1,
        "maths": marks2,
        "english": marks3
    }

    students.append(student)

    print("Student Added Successfully!")


# FUNCTION 2: Calculate Result

def calculate_result(student):

    total = (
        student["python"]
        + student["maths"]
        + student["english"]
    )

    percentage = total / 3

    if (
        student["python"] >= 33
        and student["maths"] >= 33
        and student["english"] >= 33
    ):
        result = "PASS"
    else:
        result = "FAIL"

    return total, percentage, result


# FUNCTION 3: Display All Students

def display_students():

    print("\n----- ALL STUDENTS -----")

    if len(students) == 0:
        print("No Student Records Found!")
        return

    for student in students:

        total, percentage, result = calculate_result(student)

        print("\nRoll Number:", student["roll"])
        print("Name:", student["name"])
        print("Python:", student["python"])
        print("Maths:", student["maths"])
        print("English:", student["english"])
        print("Total Marks:", total)
        print("Percentage:", round(percentage, 2), "%")
        print("Result:", result)


# FUNCTION 4: Search Student

def search_student():

    roll = input("\nEnter Roll Number to Search: ")

    for student in students:

        if student["roll"] == roll:

            print("\nStudent Found!")

            total, percentage, result = calculate_result(student)

            print("Name:", student["name"])
            print("Total Marks:", total)
            print("Percentage:", round(percentage, 2))
            print("Result:", result)

            return

    print("Student Not Found!")


# FUNCTION 5: Delete Student

def delete_student():

    roll = input("\nEnter Roll Number to Delete: ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


# FUNCTION 6: Topper Student

def find_topper():

    if len(students) == 0:
        print("No Student Records Available!")
        return

    topper = students[0]

    for student in students:

        total, percentage, result = calculate_result(student)

        topper_total, _, _ = calculate_result(topper)

        if total > topper_total:
            topper = student

    print("\n----- TOPPER DETAILS -----")

    total, percentage, result = calculate_result(topper)

    print("Name:", topper["name"])
    print("Roll Number:", topper["roll"])
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2))


# FUNCTION 7: Main Menu

def main():

    while True:

        print("\n================================")
        print("    STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Find Topper")
        print("6. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            find_topper()

        elif choice == "6":
            print("Thank You!")
            print("Project Closed Successfully.")
            break

        else:
            print("Invalid Choice! Try Again.")

            # Start Project

main()

