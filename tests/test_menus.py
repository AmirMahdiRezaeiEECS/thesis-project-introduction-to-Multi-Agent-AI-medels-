from src.storage.json_storage import JsonStorage
from src.entities.student import Student
from src.entities.professor import Professor
from src.interfaces.student_menu import show_student_menu
from src.interfaces.professor_menu import show_professor_menu

def test_menus(monkeypatch):
    storage = JsonStorage()
    
    # Test student menu
    student_data = {"name": "علی رضایی", "student_code": "0000", "password": "0000"}
    student = Student(student_data)
    
    # Simulate student menu inputs: view courses (1), exit (5)
    inputs = iter(["1", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    show_student_menu(student)
    
    # Test professor menu
    professor_data = {"name": "دکتر حسینی", "teacher_code": "1111", "password": "1111"}
    professor = Professor(professor_data)
    
    # Simulate professor menu inputs: view thesis requests (1), exit (4)
    inputs = iter(["1", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    show_professor_menu(professor)
    
    print("Menu tests passed!")