"""
defense.py

Defense session and committee details.
"""
from src.storage.json_storage import JsonStorage

class Defense:
    def __init__(self, data):
        self.student_code = data["student_code"]
        self.course_id = data["course_id"]
        self.title = data["title"]
        self.year = data["year"]
        self.semester = data["semester"]
        self.supervisor = data["supervisor"]
        self.judges = data.get("judges", [])
        self.score = data.get("score")
        self.files = data.get("files", [])
        self.keywords = data.get("keywords", [])
        self.storage = JsonStorage()

    def submit(self):
        """Submit defense to defended_thesis.json."""
        return self.storage.update_json("defended_thesis.json", {
            "student_code": self.student_code,
            "course_id": self.course_id,
            "title": self.title,
            "year": self.year,
            "semester": self.semester,
            "supervisor": self.supervisor,
            "judges": self.judges,
            "score": self.score,
            "files": self.files,
            "keywords": self.keywords
        })

    def assign_score(self, score):
        """Assign score to defended thesis."""
        theses = self.storage.read_json("defended_thesis.json")
        for t in theses:
            if t["student_code"] == self.student_code and t["course_id"] == self.course_id:
                t["score"] = score
        self.storage.write_json("defended_thesis.json", theses)