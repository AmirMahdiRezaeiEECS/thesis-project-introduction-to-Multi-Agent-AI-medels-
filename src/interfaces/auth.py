from src.storage.json_storage import JsonStorage
from src.entities.student import Student
from src.entities.professor import Professor

class Auth:
    def __init__(self, storage):
        self.storage = storage

    def login(self, user_type):
        """Login user based on type (student or professor)."""
        if user_type == "student":
            filename = "students.json"
            code_field = "student_code"
            class_obj = Student
        elif user_type == "professor":
            filename = "professors.json"
            code_field = "teacher_code"
            class_obj = Professor
        else:
            raise ValueError("Invalid user type")

        code = input(f"Enter your {user_type} code: ")
        password = input("Enter your password: ")

        users = self.storage.read_json(filename)
        for user_data in users:
            if user_data.get(code_field) == code and user_data.get("password") == password:
                return class_obj(user_data)  # Create object from data
        print("Invalid code or password. Try again.")
        return self.login(user_type)  # Retry

    def sign_in(self):
        """Mock sign-in, redirect to login."""
        print("Registration is closed. Please log in.")
        role = input("Are you a student or professor? (student/professor): ").lower()
        return self.login(role)



"""
نسخه قبلی (جهت اطمینان)
from src.storage.json_storage import JsonStorage
from src.entities.student import Student  # بعداً این کلاس رو می‌سازیم
from src.entities.professor import Professor  # بعداً این کلاس رو می‌سازیم

class Auth:
    def __init__(self, storage):
        self.storage = storage

    def login(self, user_type):
        #Login user based on type (student or professor).
        if user_type == "student":
            filename = "students.json"
            code_field = "student_code"
            class_obj = Student
        elif user_type == "professor":
            filename = "professors.json"
            code_field = "teacher_code"
            class_obj = Professor
        else:
            raise ValueError("Invalid user type")

        code = input(f"Enter your {user_type} code: ")
        password = input("Enter your password: ")

        users = self.storage.read_json(filename)
        for user_data in users:
            if user_data.get(code_field) == code and user_data.get("password") == password:
                return class_obj(user_data)  # Create object from data
        print("Invalid code or password. Try again.")
        return self.login(user_type)  # Retry

    def sign_in(self):
        #Mock sign-in, redirect to login.
        print("Registration is closed. Please log in.")
        role = input("Are you a student or professor? (student/professor): ").lower()
        return self.login(role)
        """