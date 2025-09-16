"""
course.py

Course class representing a course in the system.
"""
class Course:
    def __init__(self, data):
        self.course_id = data["course_id"]
        self.title = data["course_title"]
        self.professor_code = data["professor_code"]
        self.year = data["year"]
        self.semester = data["semester"]
        self.capacity = data["capacity"]
        self.resources = data["resources"]
        self.sessions = data["sessions"]
        self.unit = data["unit"]

    def has_capacity(self):
        """Check if course has capacity."""
        return self.capacity > 0