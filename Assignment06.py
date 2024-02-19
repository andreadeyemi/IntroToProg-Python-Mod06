import json

# --- Constants: ---
MENU: str = '''
---- Course Registration Program ----
Select from the following menu:  
1. Register a Student for a Course
2. Show current data
3. Save data to a file
4. Exit the program
----------------------------------------
'''
FILE_NAME: str = "Enrollments.json"

# --- Variables: ---
menu_choice: str = ""
students: list = []

# --- Classes and Functions: ---
class FileProcessor:
    """Processes file read and write operations."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file and loads it into a provided list."""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages("File not found. A new file will be created.", e)
        except Exception as e:
            IO.output_error_messages("An error occurred while reading the file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list to a file in JSON format."""
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file)
            print("Data successfully saved to file.")
        except Exception as e:
            IO.output_error_messages("An error occurred while writing to the file.", e)

class IO:
    """Handles input and output operations."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays error messages."""
        print(f"ERROR: {message}")
        if error:
            print(f"Details: {error}")

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu."""
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """Prompts user for a menu choice and returns it."""
        return input("What would you like to do? ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays current students and their courses."""
        print("-" * 40)
        for student in student_data:
            print(f'{student["FirstName"]} {student["LastName"]} is registered for {student["CourseName"]}.')
        print("-" * 40)

    @staticmethod
    def input_student_data():
        """Prompts user for student data and returns it as a dictionary."""
        try:
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            course_name = input("Enter the course name: ")
            return {"FirstName": first_name, "LastName": last_name, "CourseName": course_name}
        except Exception as e:
            IO.output_error_messages("An error occurred while capturing student data.", e)
            return {}

# --- Main Processing: ---
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        student_data = IO.input_student_data()
        if student_data:
            students.append(student_data)
            print(f"{student_data['FirstName']} {student_data['LastName']} has been registered for {student_data['CourseName']}.")
    elif menu_choice == "2":
        IO.output_student_courses(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid option, please choose from 1 to 4.")

print("Program Ended.")
