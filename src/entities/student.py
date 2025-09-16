"""
student.py

Student-specific logic and extensions of User.
"""
from src.entities.user import User
from src.storage.json_storage import JsonStorage
import os
from datetime import datetime

class Student(User):
    def __init__(self, data):
        super().__init__(
            name=data["name"],
            code=data["student_code"],
            password=data["password"]
        )
        self.storage = JsonStorage()

    def view_courses(self):
        """Display available courses with capacity."""
        courses = self.storage.read_json("courses.json")
        print("\nدرس‌های موجود:")
        for course in courses:
            if course.get("capacity", 0) > 0:
                print(f"شناسه: {course['course_id']}, عنوان: {course['course_title']}, "
                      f"استاد: {course['professor_code']}, ظرفیت: {course['capacity']}")

    def submit_thesis_request(self, course_id):
        """Submit a thesis request (auto-approved in MVP)."""
        courses = self.storage.read_json("courses.json")
        course = next((c for c in courses if c["course_id"] == course_id), None)
        if not course:
            print("درس پیدا نشد!")
            return False
        if course.get("capacity", 0) <= 0:
            print("ظرفیت درس پر شده است!")
            return False

        # Check for duplicate thesis request
        theses = self.storage.read_json("thesis.json")
        if any(t["student_code"] == self.code and t["course_id"] == course_id for t in theses):
            print("شما قبلاً برای این درس درخواست داده‌اید!")
            return False

        thesis = {
            "student_code": self.code,
            "course_id": course_id,
            "request_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "approved",  # Auto-approved in MVP
            "approval_date": datetime.now().strftime("%Y-%m-%d"),
            "defense_date": None,
            "files": [],
            "score": None,
            "judges": []
        }
        return self.storage.update_json("thesis.json", thesis)

    def submit_defense_request(self, title, keywords, pdf_path, course_id):
        """Submit a defense request for a specific course."""
        if not pdf_path:  # Simple validation instead of checking file existence
            print("مسیر فایل PDF نمی‌تواند خالی باشد!")
            return False

        thesis = self.storage.read_json("thesis.json")
        thesis_entry = next((t for t in thesis if t["student_code"] == self.code and t["course_id"] == course_id), None)
        if not thesis_entry or thesis_entry["status"] != "approved":
            print("ابتدا باید درخواست پایان‌نامه تأیید شده برای این درس داشته باشید!")
            return False

        defense = {
            "student_code": self.code,
            "course_id": thesis_entry["course_id"],
            "title": title,
            "year": datetime.now().year,
            "semester": "اول",  # Simplified for MVP
            "supervisor": next(c["professor_code"] for c in self.storage.read_json("courses.json") 
                              if c["course_id"] == thesis_entry["course_id"]),
            "judges": [],
            "score": None,
            "files": [pdf_path],
            "keywords": keywords
        }
        thesis_entry["status"] = "defending"
        self.storage.write_json("thesis.json", thesis)
        return self.storage.update_json("defended_thesis.json", defense)

    def search_theses(self, search_term):
        """Search defended theses by title, author, or keywords."""
        theses = self.storage.read_json("defended_thesis.json")
        results = [
            t for t in theses
            if (search_term.lower() in t["title"].lower() or
                search_term.lower() in t["student_code"].lower() or
                any(search_term.lower() in k.lower() for k in t["keywords"]))
        ]
        for thesis in results:
            print(f"عنوان: {thesis['title']}, نویسنده: {thesis['student_code']}, "
                  f"سال: {thesis['year']}, نیمسال: {thesis['semester']}, "
                  f"استاد راهنما: {thesis['supervisor']}, داوران: {thesis['judges']}, "
                  f"فایل: {thesis['files']}")

"""
from src.entities.user import User
from src.storage.json_storage import JsonStorage
import os
from datetime import datetime

class Student(User):
    def __init__(self, data):
        super().__init__(
            name=data["name"],
            code=data["student_code"],
            password=data["password"]
        )
        self.storage = JsonStorage()

    def view_courses(self):
        #Display available courses with capacity.
        courses = self.storage.read_json("courses.json")
        print("\nدرس‌های موجود:")
        for course in courses:
            if course.get("capacity", 0) > 0:
                print(f"شناسه: {course['course_id']}, عنوان: {course['course_title']}, "
                      f"استاد: {course['professor_code']}, ظرفیت: {course['capacity']}")

    def submit_thesis_request(self, course_id):
        #Submit a thesis request (auto-approved in MVP).
        courses = self.storage.read_json("courses.json")
        course = next((c for c in courses if c["course_id"] == course_id), None)
        if not course:
            print("درس پیدا نشد!")
            return False
        if course.get("capacity", 0) <= 0:
            print("ظرفیت درس پر شده است!")
            return False

        # Check for duplicate thesis request
        theses = self.storage.read_json("thesis.json")
        if any(t["student_code"] == self.code and t["course_id"] == course_id for t in theses):
            print("شما قبلاً برای این درس درخواست داده‌اید!")
            return False

        thesis = {
            "student_code": self.code,
            "course_id": course_id,
            "request_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "approved",  # Auto-approved in MVP
            "approval_date": datetime.now().strftime("%Y-%m-%d"),
            "defense_date": None,
            "files": [],
            "score": None,
            "judges": []
        }
        return self.storage.update_json("thesis.json", thesis)

    def submit_defense_request(self, title, keywords, pdf_path):
        #Submit a defense request.
        if not pdf_path:  # Simple validation instead of checking file existence
            print("مسیر فایل PDF نمی‌تواند خالی باشد!")
            return False

        thesis = self.storage.read_json("thesis.json")
        thesis_entry = next((t for t in thesis if t["student_code"] == self.code), None)
        if not thesis_entry or thesis_entry["status"] != "approved":
            print("ابتدا باید درخواست پایان‌نامه تأیید شده داشته باشید!")
            return False

        defense = {
            "student_code": self.code,
            "course_id": thesis_entry["course_id"],
            "title": title,
            "year": datetime.now().year,
            "semester": "اول",  # Simplified for MVP
            "supervisor": next(c["professor_code"] for c in self.storage.read_json("courses.json") 
                              if c["course_id"] == thesis_entry["course_id"]),
            "judges": [],
            "score": None,
            "files": [pdf_path],
            "keywords": keywords
        }
        thesis_entry["status"] = "defending"
        self.storage.write_json("thesis.json", thesis)
        return self.storage.update_json("defended_thesis.json", defense)

    def search_theses(self, search_term):
        #Search defended theses by title, author, or keywords.
        theses = self.storage.read_json("defended_thesis.json")
        results = [
            t for t in theses
            if (search_term.lower() in t["title"].lower() or
                search_term.lower() in t["student_code"].lower() or
                any(search_term.lower() in k.lower() for k in t["keywords"]))
        ]
        for thesis in results:
            print(f"عنوان: {thesis['title']}, نویسنده: {thesis['student_code']}, "
                  f"سال: {thesis['year']}, نیمسال: {thesis['semester']}, "
                  f"استاد راهنما: {thesis['supervisor']}, داوران: {thesis['judges']}, "
                  f"فایل: {thesis['files']}")
"""


"""

نسخه قبل تر از نسخه قبلی : 
from src.entities.user import User
from src.storage.json_storage import JsonStorage
import os
from datetime import datetime

class Student(User):
    def __init__(self, data):
        super().__init__(
            name=data["name"],
            code=data["student_code"],
            password=data["password"]
        )
        self.storage = JsonStorage()

    def view_courses(self):
        #Display available courses with capacity
        courses = self.storage.read_json("courses.json")
        print("\nدرس‌های موجود:")
        for course in courses:
            if course.get("capacity", 0) > 0:
                print(f"شناسه: {course['course_id']}, عنوان: {course['course_title']}, "
                      f"استاد: {course['professor_code']}, ظرفیت: {course['capacity']}")

    def submit_thesis_request(self, course_id):
        #Submit a thesis request (auto-approved in MVP)
        courses = self.storage.read_json("courses.json")
        course = next((c for c in courses if c["course_id"] == course_id), None)
        if not course:
            print("درس پیدا نشد!")
            return False
        if course.get("capacity", 0) <= 0:
            print("ظرفیت درس پر شده است!")
            return False

        thesis = {
            "student_code": self.code,
            "course_id": course_id,
            "request_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "approved",  # Auto-approved in MVP
            "approval_date": datetime.now().strftime("%Y-%m-%d"),
            "defense_date": None,
            "files": [],
            "score": None,
            "judges": []
        }
        return self.storage.update_json("thesis.json", thesis)

    def submit_defense_request(self, title, keywords, pdf_path):
        #Submit a defense request.
        if not os.path.exists(pdf_path):
            print("فایل PDF پیدا نشد!")
            return False

        thesis = self.storage.read_json("thesis.json")
        thesis_entry = next((t for t in thesis if t["student_code"] == self.code), None)
        if not thesis_entry or thesis_entry["status"] != "approved":
            print("ابتدا باید درخواست پایان‌نامه تأیید شده داشته باشید!")
            return False

        defense = {
            "student_code": self.code,
            "course_id": thesis_entry["course_id"],
            "title": title,
            "year": datetime.now().year,
            "semester": "اول",  # Simplified for MVP
            "supervisor": next(c["professor_code"] for c in self.storage.read_json("courses.json") 
                              if c["course_id"] == thesis_entry["course_id"]),
            "judges": [],
            "score": None,
            "files": [pdf_path],
            "keywords": keywords
        }
        thesis_entry["status"] = "defending"
        self.storage.write_json("thesis.json", thesis)
        return self.storage.update_json("defended_thesis.json", defense)

    def search_theses(self, search_term):
        #Search defended theses by title, author, or keywords.
        theses = self.storage.read_json("defended_thesis.json")
        results = [
            t for t in theses
            if (search_term.lower() in t["title"].lower() or
                search_term.lower() in t["student_code"].lower() or
                any(search_term.lower() in k.lower() for k in t["keywords"]))
        ]
        for thesis in results:
            print(f"عنوان: {thesis['title']}, نویسنده: {thesis['student_code']}, "
                  f"سال: {thesis['year']}, نیمسال: {thesis['semester']}, "
                  f"استاد راهنما: {thesis['supervisor']}, داوران: {thesis['judges']}, "
                  f"فایل: {thesis['files']}")
                  
"""