"""
student_menu.py

CLI menu for student features.

ماژول StudentMenu:
    متد show_menu(student):
        حلقه تا زمانی که کاربر خروج انتخاب کنه:
            نمایش گزینه‌ها:
                1. مشاهده درس‌های موجود
                2. ثبت درخواست پایان‌نامه
                3. ثبت درخواست دفاع
                4. جست‌وجوی پایان‌نامه‌ها
                5. خروج
            گرفتن انتخاب کاربر
            اگر 1: فراخوانی student.view_courses()
            اگر 2: گرفتن course_id و فراخوانی student.submit_thesis_request()
            اگر 3: گرفتن title, keywords, pdf_path و فراخوانی student.submit_defense_request()
            اگر 4: گرفتن search_term و فراخوانی student.search_theses()
            اگر 5: خروج
            اگر نامعتبر: نمایش خطا و تکرار
            
    
"""

from src.entities.student import Student

def show_student_menu(student: Student):
    """Show CLI menu for student and handle actions."""
    while True:
        print("\nمنوی دانشجو:")
        print("1. مشاهده درس‌های موجود")
        print("2. ثبت درخواست پایان‌نامه")
        print("3. ثبت درخواست دفاع")
        print("4. جست‌وجوی پایان‌نامه‌ها")
        print("5. خروج")
        choice = input("انتخاب شما: ")

        if choice == "1":
            student.view_courses()
        elif choice == "2":
            course_id = input("شناسه درس را وارد کنید: ")
            if student.submit_thesis_request(course_id):
                print("درخواست پایان‌نامه ثبت شد.")
        elif choice == "3":
            course_id = input("شناسه درس را وارد کنید: ")
            title = input("عنوان پایان‌نامه: ")
            keywords = input("کلمات کلیدی (با کاما جدا کنید): ").split(",")
            pdf_path = input("مسیر فایل PDF: ")
            if student.submit_defense_request(title, [k.strip() for k in keywords], pdf_path, course_id):
                print("درخواست دفاع ثبت شد.")
            else:
                print("ثبت درخواست دفاع ناموفق بود!")
        elif choice == "4":
            search_term = input("عبارت جست‌وجو: ")
            student.search_theses(search_term)
        elif choice == "5":
            print("خروج از منوی دانشجو.")
            break
        else:
            print("انتخاب نامعتبر! لطفاً دوباره امتحان کنید.")

"""

from src.entities.student import Student

def show_student_menu(student: Student):
    #Show CLI menu for student and handle actions.
    while True:
        print("\nمنوی دانشجو:")
        print("1. مشاهده درس‌های موجود")
        print("2. ثبت درخواست پایان‌نامه")
        print("3. ثبت درخواست دفاع")
        print("4. جست‌وجوی پایان‌نامه‌ها")
        print("5. خروج")
        choice = input("انتخاب شما: ")

        if choice == "1":
            student.view_courses()
        elif choice == "2":
            course_id = input("شناسه درس را وارد کنید: ")
            if student.submit_thesis_request(course_id):
                print("درخواست پایان‌نامه ثبت شد.")
        elif choice == "3":
            title = input("عنوان پایان‌نامه: ")
            keywords = input("کلمات کلیدی (با کاما جدا کنید): ").split(",")
            pdf_path = input("مسیر فایل PDF: ")
            if student.submit_defense_request(title, [k.strip() for k in keywords], pdf_path):
                print("درخواست دفاع ثبت شد.")
        elif choice == "4":
            search_term = input("عبارت جست‌وجو: ")
            student.search_theses(search_term)
        elif choice == "5":
            print("خروج از منوی دانشجو.")
            break
        else:
            print("انتخاب نامعتبر! لطفاً دوباره امتحان کنید.")

"""


"""
نسخه قبلی : 
def student_menu(student_code: str):
    print(f"Student menu for {student_code} - TODO")

"""
