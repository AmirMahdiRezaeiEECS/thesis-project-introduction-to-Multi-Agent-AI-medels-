from src.storage.json_storage import JsonStorage
from src.interfaces.welcome import welcome_and_role_determination
from src.entities.student import Student

def test_main(monkeypatch, capsys):
    """Test the main program flow."""
    storage = JsonStorage()
    
    # Simulate login as student (select role 1, code 0000, password 0000)
    inputs = iter(["1", "0000", "0000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user = welcome_and_role_determination(storage)
    assert isinstance(user, Student), "Main should return a Student object"
    assert user.code == "0000", "Student code incorrect"
    
    # Check welcome message
    captured = capsys.readouterr()
    assert "خوش آمدید به سیستم مدیریت پایان‌نامه‌ها!" in captured.out
    print("Main program test passed!")