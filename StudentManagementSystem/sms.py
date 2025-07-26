print("\nStudent Management System ")
print("-----------------------------------------------------------------------------")
students={}
while True:
    print("\n 1. View Student \n 2. Add Student \n 3. Update Student Grade \n 4. Delete Student \n 5. List All Students \n 6. Exit")

    choice=int(input("Enter your choice from above : "))

    if choice==1:
        roll_number=input("Enter Student's Roll Number : ")
        if roll_number in students:
            student=students[roll_number]
            print(f"Roll Number : {roll_number}")
            print(f"Name : {student['name']}")
            print(f"CGPA : {student['CGPA']}")
        else:
            print("Student Not Found")

    elif choice==2:
        roll_number=input("Enter Student's Roll Number : ")
        if roll_number in students:
            print("Student with this roll number already exist")
        else:
            name=input("Enter Student's Name : ")
            cgpa=input("Enter Student's CGPA : ")
            students[roll_number]={"name":name,"cgpa":cgpa}
            print("Student Added Successfully")

    elif choice==3:
        roll_number = input("Enter Student's Roll Number : ")
        if roll_number in students:
            new_cgpa=input("Enter New CGPA : ")
            students[roll_number]["grade"] = new_cgpa
            print("Grade updated successfully!")
        else:
            print("Student not found.")

    elif choice==4:
        roll_number = input("Enter Student's Roll Number : ")
        if  roll_number in students:
            del students[roll_number]
            print("Record Deleted Successfully ! ")
        else:
            print("Student Not Found")

    elif choice==5:
        if not students:
            print("No students in the system.")
        else:
            print("List of Students:")
            for roll_number, student in students.items():
                print(f"Roll Number: {roll_number}, Name: {student['name']}, CGPA: {student['cgpa']}")


    elif choice=="6":
        print("Exiting ..................")
        break

    else:
        print("Invalid Input")