from src.storage.json_storage import JsonStorage
from src.entities.student import Student
from src.entities.professor import Professor
from src.entities.course import Course
from src.entities.thesis import Thesis
from src.entities.defense import Defense

def test_entities():
    storage = JsonStorage()
    
    # Test Student
    student_data = {"name": "علی رضایی", "student_code": "0000", "password": "0000"}
    student = Student(student_data)
    assert student.name == "علی رضایی", "Student name incorrect"
    
    # Test Course
    course_data = {
        "course_id": "C001", "course_title": "هوش مصنوعی پیشرفته",
        "professor_code": "1111", "year": 2025, "semester": "اول",
        "capacity": 10, "resources": ["کتاب"], "sessions": 10, "unit": 3
    }
    course = Course(course_data)
    assert course.has_capacity(), "Course should have capacity"
    
    # Test Thesis submission
    thesis_data = {
        "student_code": "0000", "course_id": "C001", "request_date": "2025-09-16",
        "status": "approved", "approval_date": "2025-09-16",
        "defense_date": None, "files": [], "score": None, "judges": []
    }
    thesis = Thesis(thesis_data)
    assert thesis.submit(), "Failed to submit thesis"
    
    # Test Defense submission
    defense_data = {
        "student_code": "0000", "course_id": "C001", "title": "کاربرد هوش مصنوعی",
        "year": 2025, "semester": "اول", "supervisor": "1111",
        "judges": [], "score": None, "files": ["uploads/0000_هوش_مصنوعی_پیشرفته_thesis.pdf"],
        "keywords": ["هوش مصنوعی"]
    }
    defense = Defense(defense_data)
    assert defense.submit(), "Failed to submit defense"
    
    # Test Professor
    professor_data = {"name": "دکتر حسینی", "teacher_code": "1111", "password": "1111"}
    professor = Professor(professor_data)
    professor.search_theses("هوش مصنوعی")
    
    print("All entity tests passed!")

if __name__ == "__main__":
    test_entities()