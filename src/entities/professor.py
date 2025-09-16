"""
professor.py

Professor-specific logic (advisor/examiner).
"""
from src.entities.user import User
from src.storage.json_storage import JsonStorage
from datetime import datetime

class Professor(User):
    def __init__(self, data):
        super().__init__(
            name=data["name"],
            code=data["teacher_code"],
            password=data["password"]
        )
        self.storage = JsonStorage()

    def view_thesis_requests(self):
        """Display thesis requests for this professor (mocked in MVP)."""
        theses = self.storage.read_json("thesis.json")
        print("\nدرخواست‌های پایان‌نامه:")
        for thesis in theses:
            if next((c["professor_code"] for c in self.storage.read_json("courses.json") 
                     if c["course_id"] == thesis["course_id"]), None) == self.code:
                print(f"دانشجو: {thesis['student_code']}, درس: {thesis['course_id']}, "
                      f"وضعیت: {thesis['status']}")

    def manage_defense_requests(self):
        """Manage defense requests (approve, set date, assign judges)."""
        theses = self.storage.read_json("defended_thesis.json")
        print("\nدرخواست‌های دفاع:")
        for i, thesis in enumerate(theses, 1):
            if thesis["supervisor"] == self.code:
                print(f"{i}. دانشجو: {thesis['student_code']}, عنوان: {thesis['title']}")

        choice = input("شماره درخواست را انتخاب کنید (یا 0 برای لغو): ")
        if choice == "0":
            return False

        try:
            index = int(choice) - 1
            if index < 0 or index >= len(theses):
                print("انتخاب نامعتبر!")
                return False
        except ValueError:
            print("ورودی نامعتبر!")
            return False

        action = input("اقدام: (1: تأیید، 2: رد): ")
        if action == "1":
            defense_date = input("تاریخ دفاع (YYYY-MM-DD): ")
            judges = input("کد داوران (با کاما جدا کنید): ").split(",")
            theses[index]["defense_date"] = defense_date
            theses[index]["judges"] = [j.strip() for j in judges]
            self.storage.write_json("defended_thesis.json", theses)
            
            # Update thesis.json
            thesis_data = self.storage.read_json("thesis.json")
            for t in thesis_data:
                if t["student_code"] == theses[index]["student_code"] and \
                   t["course_id"] == theses[index]["course_id"]:
                    t["status"] = "defending"
                    t["defense_date"] = defense_date
                    t["judges"] = judges
            self.storage.write_json("thesis.json", thesis_data)
            print("درخواست دفاع تأیید شد.")
            return True
        elif action == "2":
            thesis_data = self.storage.read_json("thesis.json")
            for t in thesis_data:
                if t["student_code"] == theses[index]["student_code"] and \
                   t["course_id"] == theses[index]["course_id"]:
                    t["status"] = "rejected"
            self.storage.write_json("thesis.json", thesis_data)
            print("درخواست دفاع رد شد.")
            return True
        else:
            print("اقدام نامعتبر!")
            return False

    def search_theses(self, search_term):
        """Search defended theses (same as Student)."""
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