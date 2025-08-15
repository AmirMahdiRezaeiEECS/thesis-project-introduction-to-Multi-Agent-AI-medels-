# main_program.py — tiny menu to run v1
# main_program.py — منوی خیلی کوچک برای اجرای نسخهٔ ۱

"""
Plain summary:
- Shows a simple menu so you can create, list, or mark submitted.

خلاصهٔ ساده:
- یک منوی ساده نشان می‌دهد تا بتوانی ایجاد، فهرست یا ارسال‌شده کردن را انجام دهی.
"""

from thesis_management_system.user_commands import command_create_thesis, command_show_thesis, command_mark_submitted

def menu():
    print("""
Thesis Management — v1
سیستم مدیریت پایان‌نامه — نسخه ۱

1) Create a thesis record (ایجاد رکورد)
2) List all thesis records (نمایش همه)
3) Mark a thesis as submitted (علامت‌گذاری به ارسال‌شده)
0) Exit (خروج)
""")
    return input("Choose an option (یک گزینه را انتخاب کن): ").strip()

def main():
    while True:
        choice = menu()
        if choice == "1":
            command_create_thesis.run()
        elif choice == "2":
            command_show_thesis.run()
        elif choice == "3":
            command_mark_submitted.run()
        elif choice == "0":
            print("Bye! خداحافظ!")
            break
        else:
            print("Invalid choice. انتخاب نامعتبر.")

if __name__ == "__main__":
    main()
