"""
professor_menu.py

CLI menu for professor features.

ماژول ProfessorMenu:
    متد show_menu(professor):
        حلقه تا زمانی که کاربر خروج انتخاب کنه:
            نمایش گزینه‌ها:
                1. مشاهده درخواست‌های پایان‌نامه
                2. مدیریت درخواست‌های دفاع
                3. جست‌وجوی پایان‌نامه‌ها
                4. خروج
            گرفتن انتخاب کاربر
            اگر 1: فراخوانی professor.view_thesis_requests()
            اگر 2: فراخوانی professor.manage_defense_requests()
            اگر 3: گرفتن search_term و فراخوانی professor.search_theses()
            اگر 4: خروج
            اگر نامعتبر: نمایش خطا و تکرار
            
"""

from src.entities.professor import Professor

def show_professor_menu(professor: Professor):
    """Show CLI menu for professor and handle actions."""
    while True:
        print("\nمنوی استاد:")
        print("1. مشاهده درخواست‌های پایان‌نامه")
        print("2. مدیریت درخواست‌های دفاع")
        print("3. جست‌وجوی پایان‌نامه‌ها")
        print("4. خروج")
        choice = input("انتخاب شما: ")

        if choice == "1":
            professor.view_thesis_requests()
        elif choice == "2":
            if professor.manage_defense_requests():
                print("مدیریت درخواست دفاع انجام شد.")
        elif choice == "3":
            search_term = input("عبارت جست‌وجو: ")
            professor.search_theses(search_term)
        elif choice == "4":
            print("خروج از منوی استاد.")
            break
        else:
            print("انتخاب نامعتبر! لطفاً دوباره امتحان کنید.")
            

"""

کد قبلی : 
def professor_menu(prof_code: str):
    print(f"Professor menu for {prof_code} - TODO")

"""