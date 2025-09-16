"""
thesis.py

Thesis class (request + status metadata).
"""
from src.storage.json_storage import JsonStorage
from datetime import datetime

class Thesis:
    def __init__(self, data):
        self.student_code = data["student_code"]
        self.course_id = data["course_id"]
        self.request_date = data["request_date"]
        self.status = data["status"]
        self.approval_date = data.get("approval_date")
        self.defense_date = data.get("defense_date")
        self.files = data.get("files", [])
        self.score = data.get("score")
        self.judges = data.get("judges", [])
        self.storage = JsonStorage()

    def submit(self):
        """Submit thesis request to thesis.json."""
        return self.storage.update_json("thesis.json", {
            "student_code": self.student_code,
            "course_id": self.course_id,
            "request_date": self.request_date,
            "status": self.status,
            "approval_date": self.approval_date,
            "defense_date": self.defense_date,
            "files": self.files,
            "score": self.score,
            "judges": self.judges
        })

    def update_status(self, status, defense_date=None, judges=None):
        """Update thesis status and related fields."""
        theses = self.storage.read_json("thesis.json")
        for t in theses:
            if t["student_code"] == self.student_code and t["course_id"] == self.course_id:
                t["status"] = status
                if defense_date:
                    t["defense_date"] = defense_date
                if judges:
                    t["judges"] = judges
        self.storage.write_json("thesis.json", theses)