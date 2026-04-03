print("Welcome to Collection Manipulator")

# Collections
students = ["Alice", "Bob", "Charlie"]
marks = (85, 90, 78, 90)
subjects = {"Math", "Science", "English"}
student_data = {"Alice": 85, "Bob": 90, "Charlie": 78}

while True:
    print("\n========== MAIN MENU ==========")
    print("1. List Operations")
    print("2. Tuple Operations")
    print("3. Set Operations")
    print("4. Dictionary Operations")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # =========================
    # LIST OPERATIONS
    # =========================
    if choice == "1":
        print("\n--- List Operations ---")
        print("Current List:", students)
        print("1. Add Student")
        print("2. Insert Student")
        print("3. Remove Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Sort List")
        print("7. Reverse List")
        print("8. Count Students")
        print("9. Display Students")

        list_choice = input("Enter your choice: ")

        if list_choice == "1":
            name = input("Enter student name to add: ")
            students.append(name)
            print("Student added successfully!")

        elif list_choice == "2":
            name = input("Enter student name to insert: ")
            position = int(input("Enter position: "))
            students.insert(position, name)
            print("Student inserted successfully!")

        elif list_choice == "3":
            name = input("Enter student name to remove: ")
            if name in students:
                students.remove(name)
                print("Student removed successfully!")
            else:
                print("Student not found!")

        elif list_choice == "4":
            old_name = input("Enter student name to update: ")
            if old_name in students:
                new_name = input("Enter new name: ")
                index = students.index(old_name)
                students[index] = new_name
                print("Student updated successfully!")
            else:
                print("Student not found!")

        elif list_choice == "5":
            name = input("Enter student name to search: ")
            if name in students:
                print(name, "found in list.")
            else:
                print("Student not found!")

        elif list_choice == "6":
            students.sort()
            print("List sorted successfully!")

        elif list_choice == "7":
            students.reverse()
            print("List reversed successfully!")

        elif list_choice == "8":
            print("Total students:", len(students))

        elif list_choice == "9":
            print("Student List:", students)

        else:
            print("Invalid choice!")

    # =========================
    # TUPLE OPERATIONS
    # =========================
    elif choice == "2":
        print("\n--- Tuple Operations ---")
        print("Current Tuple:", marks)
        print("1. Display Tuple")
        print("2. Find Maximum")
        print("3. Find Minimum")
        print("4. Find Sum")
        print("5. Find Average")
        print("6. Search Mark")
        print("7. Count Occurrence")
        print("8. Convert to List")

        tuple_choice = input("Enter your choice: ")

        if tuple_choice == "1":
            print("Marks Tuple:", marks)

        elif tuple_choice == "2":
            print("Maximum Marks:", max(marks))

        elif tuple_choice == "3":
            print("Minimum Marks:", min(marks))

        elif tuple_choice == "4":
            print("Sum of Marks:", sum(marks))

        elif tuple_choice == "5":
            print("Average Marks:", sum(marks) / len(marks))

        elif tuple_choice == "6":
            mark = int(input("Enter mark to search: "))
            if mark in marks:
                print(mark, "found in tuple.")
            else:
                print("Mark not found!")

        elif tuple_choice == "7":
            mark = int(input("Enter mark to count: "))
            print(mark, "appears", marks.count(mark), "time(s)")

        elif tuple_choice == "8":
            marks_list = list(marks)
            print("Converted List:", marks_list)

        else:
            print("Invalid choice!")

    # =========================
    # SET OPERATIONS
    # =========================
    elif choice == "3":
        print("\n--- Set Operations ---")
        print("Current Set:", subjects)
        print("1. Add Subject")
        print("2. Remove Subject")
        print("3. Search Subject")
        print("4. Union")
        print("5. Intersection")
        print("6. Difference")
        print("7. Display Set")

        set_choice = input("Enter your choice: ")

        if set_choice == "1":
            subject = input("Enter subject to add: ")
            subjects.add(subject)
            print("Subject added successfully!")

        elif set_choice == "2":
            subject = input("Enter subject to remove: ")
            if subject in subjects:
                subjects.remove(subject)
                print("Subject removed successfully!")
            else:
                print("Subject not found!")

        elif set_choice == "3":
            subject = input("Enter subject to search: ")
            if subject in subjects:
                print(subject, "found in set.")
            else:
                print("Subject not found!")

        elif set_choice == "4":
            other_set = set(input("Enter subjects separated by comma: ").split(","))
            print("Union Result:", subjects.union(other_set))

        elif set_choice == "5":
            other_set = set(input("Enter subjects separated by comma: ").split(","))
            print("Intersection Result:", subjects.intersection(other_set))

        elif set_choice == "6":
            other_set = set(input("Enter subjects separated by comma: ").split(","))
            print("Difference Result:", subjects.difference(other_set))

        elif set_choice == "7":
            print("Subjects Set:", subjects)

        else:
            print("Invalid choice!")

    # =========================
    # DICTIONARY OPERATIONS
    # =========================
    elif choice == "4":
        print("\n--- Dictionary Operations ---")
        print("Current Dictionary:", student_data)
        print("1. Add Student Marks")
        print("2. Update Student Marks")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display Keys")
        print("6. Display Values")
        print("7. Display Items")
        print("8. Display Dictionary")

        dict_choice = input("Enter your choice: ")

        if dict_choice == "1":
            name = input("Enter student name: ")
            mark = int(input("Enter marks: "))
            student_data[name] = mark
            print("Student added successfully!")

        elif dict_choice == "2":
            name = input("Enter student name to update: ")
            if name in student_data:
                new_mark = int(input("Enter new marks: "))
                student_data[name] = new_mark
                print("Marks updated successfully!")
            else:
                print("Student not found!")

        elif dict_choice == "3":
            name = input("Enter student name to delete: ")
            if name in student_data:
                del student_data[name]
                print("Student deleted successfully!")
            else:
                print("Student not found!")

        elif dict_choice == "4":
            name = input("Enter student name to search: ")
            if name in student_data:
                print(name, "has", student_data[name], "marks")
            else:
                print("Student not found!")

        elif dict_choice == "5":
            print("Keys:", student_data.keys())

        elif dict_choice == "6":
            print("Values:", student_data.values())

        elif dict_choice == "7":
            print("Items:", student_data.items())

        elif dict_choice == "8":
            print("Dictionary:", student_data)

        else:
            print("Invalid choice!")

    # =========================
    # EXIT
    # =========================
    elif choice == "5":
        print("Thank you for using Collection Manipulator!")
        break

    else:
        print("Invalid choice! Please try again.")