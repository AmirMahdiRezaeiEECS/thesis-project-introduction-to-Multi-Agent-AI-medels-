"""
user.py

Base User class for Student and Professor.
"""

class User:
    def __init__(self, name, code, password):
        self.name = name
        self.code = code
        self.password = password