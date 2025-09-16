from src.storage.json_storage import JsonStorage
from src.interfaces.welcome import welcome_and_role_determination
from src.interfaces.student_menu import show_student_menu
from src.interfaces.professor_menu import show_professor_menu
from src.entities.student import Student
from src.entities.professor import Professor

def test_comprehensive(monkeypatch, capsys):
    storage = JsonStorage()
    
    # Simulate student login and menu
    inputs = iter([
        "1",  # Select student role
        "0000", "0000",  # Student code and password
        "1",  # View courses
        "2", "C002",  # Submit thesis request (use new course_id)
        "3", "C002", "کاربرد هوش مصنوعی در آموزش", "هوش مصنوعی,آموزش", "/Users/amirmahdi/Desktop/thesis_management_system/data/uploads/test.pdf",  # Submit defense request
        "4", "هوش مصنوعی",  # Search theses
        "5"  # Exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user = welcome_and_role_determination(storage)
    assert isinstance(user, Student), "Should login as student"
    show_student_menu(user)
    
    # Check outputs
    captured = capsys.readouterr()
    assert "درس‌های موجود" in captured.out
    assert "درخواست پایان‌نامه ثبت شد" in captured.out
    assert "درخواست دفاع ثبت شد" in captured.out
    assert "هوش مصنوعی" in captured.out
    
    # Simulate professor login and menu
    inputs = iter([
        "2",  # Select professor role
        "1111", "1111",  # Professor code and password
        "1",  # View thesis requests
        "2", "1", "1", "2025-10-01", "1111",  # Manage defense request (approve, set date, assign judge)
        "3", "هوش مصنوعی",  # Search theses
        "4"  # Exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user = welcome_and_role_determination(storage)
    assert isinstance(user, Professor), "Should login as professor"
    show_professor_menu(user)
    
    # Check outputs
    captured = capsys.readouterr()
    assert "درخواست‌های پایان‌نامه" in captured.out
    assert "درخواست دفاع تأیید شد" in captured.out
    assert "هوش مصنوعی" in captured.out
    
    print("Comprehensive test passed!")





"""
from src.storage.json_storage import JsonStorage
from src.interfaces.welcome import welcome_and_role_determination
from src.interfaces.student_menu import show_student_menu
from src.interfaces.professor_menu import show_professor_menu
from src.entities.student import Student
from src.entities.professor import Professor

def test_comprehensive(monkeypatch, capsys):
    storage = JsonStorage()
    
    # Simulate student login and menu
    inputs = iter([
        "1",  # Select student role
        "0000", "0000",  # Student code and password
        "1",  # View courses
        "2", "C002",  # Submit thesis request (use new course_id)
        "3", "کاربرد هوش مصنوعی در آموزش", "هوش مصنوعی,آموزش", "/Users/amirmahdi/Desktop/thesis_management_system/data/uploads/test.pdf",  # Submit defense request
        "4", "هوش مصنوعی",  # Search theses
        "5"  # Exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user = welcome_and_role_determination(storage)
    assert isinstance(user, Student), "Should login as student"
    show_student_menu(user)
    
    # Check outputs
    captured = capsys.readouterr()
    assert "درس‌های موجود" in captured.out
    assert "درخواست پایان‌نامه ثبت شد" in captured.out
    assert "درخواست دفاع ثبت شد" in captured.out
    assert "هوش مصنوعی" in captured.out
    
    # Simulate professor login and menu
    inputs = iter([
        "2",  # Select professor role
        "1111", "1111",  # Professor code and password
        "1",  # View thesis requests
        "2", "1", "1", "2025-10-01", "1111",  # Manage defense request (approve, set date, assign judge)
        "3", "هوش مصنوعی",  # Search theses
        "4"  # Exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user = welcome_and_role_determination(storage)
    assert isinstance(user, Professor), "Should login as professor"
    show_professor_menu(user)
    
    # Check outputs
    captured = capsys.readouterr()
    assert "درخواست‌های پایان‌نامه" in captured.out
    assert "درخواست دفاع تأیید شد" in captured.out
    assert "هوش مصنوعی" in captured.out
    
    print("Comprehensive test passed!")

"""


"""

نسخه قبلی : 
from src.storage.json_storage import JsonStorage
from src.interfaces.welcome import welcome_and_role_determination
from src.interfaces.student_menu import show_student_menu
from src.interfaces.professor_menu import show_professor_menu
from src.entities.student import Student
from src.entities.professor import Professor

def test_comprehensive(monkeypatch, capsys):
    storage = JsonStorage()
    
    # Simulate student login and menu
    inputs = iter([
        "1",  # Select student role
        "0000", "0000",  # Student code and password
        "1",  # View courses
        "2", "C001",  # Submit thesis request
        "3", "کاربرد هوش مصنوعی در آموزش", "هوش مصنوعی,آموزش", "uploads/test.pdf",  # Submit defense request
        "4", "هوش مصنوعی",  # Search theses
        "5"  # Exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user = welcome_and_role_determination(storage)
    assert isinstance(user, Student), "Should login as student"
    show_student_menu(user)
    
    # Check outputs
    captured = capsys.readouterr()
    assert "درس‌های موجود" in captured.out
    assert "درخواست پایان‌نامه ثبت شد" in captured.out
    assert "درخواست دفاع ثبت شد" in captured.out
    assert "هوش مصنوعی" in captured.out
    
    # Simulate professor login and menu
    inputs = iter([
        "2",  # Select professor role
        "1111", "1111",  # Professor code and password
        "1",  # View thesis requests
        "2", "1", "1", "2025-10-01", "1111",  # Manage defense request (approve, set date, assign judge)
        "3", "هوش مصنوعی",  # Search theses
        "4"  # Exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user = welcome_and_role_determination(storage)
    assert isinstance(user, Professor), "Should login as professor"
    show_professor_menu(user)
    
    # Check outputs
    captured = capsys.readouterr()
    assert "درخواست‌های پایان‌نامه" in captured.out
    assert "درخواست دفاع تأیید شد" in captured.out
    assert "هوش مصنوعی" in captured.out
    
    print("Comprehensive test passed!")
    
    """