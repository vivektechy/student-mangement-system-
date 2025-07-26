# Student Management System (Console-Based)

This is a simple console-based student management system implemented in Python. It allows users to add, view, update, delete, and list student records.

## Features

* **Add Student:** Add new student records with roll number, name, and CGPA.
* **View Student:** View details of a specific student by roll number.
* **Update Student CGPA:** Update the CGPA of an existing student.
* **Delete Student:** Delete a student record by roll number.
* **List All Students:** Display a list of all students in the system.
* **Simple Console Interface:** Easy-to-use menu-driven interface.

## How to Run

1.  **Save the Python code:** Save the Python code (e.g., as `student_management.py`).
2.  **Open a terminal or command prompt.**
3.  **Navigate to the directory** where you saved the file.
4.  **Run the script:** Execute the command `python student_management.py`.

## Code Explanation

### Initialization

* `students = {}`: This line initializes a dictionary named `students`. This dictionary will store student records, with roll numbers as keys and student details (name and CGPA) as values.

### Main Loop

* The `while True:` loop creates the main program loop, which keeps the system running until the user chooses to exit.
* The menu is displayed with options to view, add, update, delete, list, or exit.
* The user's choice is taken as input (an integer).

### View Student

* If the user chooses to view a student (choice `1`), the program prompts for the student's roll number.
* It checks if the roll number exists as a key in the `students` dictionary.
* If found, it displays the student's roll number, name, and CGPA.
* If not found, it prints "Student Not Found".

### Add Student

* If the user chooses to add a student (choice `2`), the program prompts for the student's roll number.
* It checks if the roll number already exists in the `students` dictionary.
* If it exists, it prints "Student with this roll number already exist".
* If it doesn't exist, it prompts for the student's name and CGPA, and adds the student record to the `students` dictionary.

### Update Student CGPA

* If the user chooses to update a student's CGPA (choice `3`), the program prompts for the student's roll number.
* It checks if the roll number exists in the `students` dictionary.
* If found, it prompts for the new CGPA and updates the student's CGPA in the dictionary.
* If not found, it prints "Student not found".

### Delete Student

* If the user chooses to delete a student (choice `4`), the program prompts for the student's roll number.
* It checks if the roll number exists in the `students` dictionary.
* If found, it deletes the student record from the dictionary.
* If not found, it prints "Student Not Found".

### List All Students

* If the user chooses to list all students (choice `5`), the program checks if the `students` dictionary is empty.
* If empty, it prints "No students in the system".
* If not empty, it iterates through the `students` dictionary and displays the roll number, name, and CGPA of each student.

### Exit

* If the user chooses to exit (choice `6`), the program prints "Exiting .................." and breaks out of the loop.

### Input Handling

* The program uses `int(input(...))` to convert user input to integers for menu choices.
* It uses `students.items()` to iterate through the dictionary and display student records.
* It uses `del students[roll_number]` to delete a student record.

### Dictionary Use

* The `students` dictionary is used to efficiently store and retrieve student records using roll numbers as keys.
* This allows for quick access to student information and ensures that roll numbers are unique.