students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        branch = input("Enter student branch: ")

        student = {
            "name": name,
            "age": age,
            "branch": branch
        }

        students.append(student)
        print("Student added successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        name = input("Enter name to search: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print(student)
                found = True

        if found == False:
            print("Student not found")

    elif choice == "4":
        name = input("Enter name to delete: ")

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                print("Student deleted")
                break
        else:
            print("Student not found")

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")
