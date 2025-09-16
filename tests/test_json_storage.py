from src.storage.json_storage import JsonStorage

def test_json_storage():
    storage = JsonStorage()
    
    # Test data
    student = {
        "name": "علی رضایی",
        "student_code": "0000",
        "password": "0000"
    }
    
    # Test writing
    assert storage.write_json("students.json", [student]), "Failed to write JSON"
    
    # Test reading
    data = storage.read_json("students.json")
    assert len(data) == 1, "Failed to read JSON"
    assert data[0]["name"] == "علی رضایی", "Incorrect data read"
    
    # Test updating
    new_student = {
        "name": "مریم حسینی",
        "student_code": "0001",
        "password": "0001"
    }
    assert storage.update_json("students.json", new_student), "Failed to update JSON"
    data = storage.read_json("students.json")
    assert len(data) == 2, "Failed to append new student"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_json_storage() 