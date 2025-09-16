#!/usr/bin/env python3

"""
Entry point for Thesis Management System CLI.
This file should import the welcome/role selection and start the CLI loop.

توضیحات:

سادگی: کد خیلی کوتاه و تمیزه، فقط ماژول‌ها رو به هم وصل می‌کنه.
ماژولاریتی: منطق اصلی توی welcome.py, student_menu.py, و professor_menu.py نگه‌داری شده.
ورود کاربر: از welcome_and_role_determination برای تشخیص نقش و ورود استفاده می‌شه.
هدایت به منو: بسته به نوع کاربر (Student یا Professor)، منوی مناسب فراخوانی می‌شه.

"""

from src.storage.json_storage import JsonStorage
from src.interfaces.welcome import welcome_and_role_determination
from src.interfaces.student_menu import show_student_menu
from src.interfaces.professor_menu import show_professor_menu
from src.entities.student import Student
from src.entities.professor import Professor

def main():
    """Main entry point for the Thesis Management System."""
    storage = JsonStorage()
    user = welcome_and_role_determination(storage)
    
    if isinstance(user, Student):
        show_student_menu(user)
    elif isinstance(user, Professor):
        show_professor_menu(user)

if __name__ == "__main__":
    main()

