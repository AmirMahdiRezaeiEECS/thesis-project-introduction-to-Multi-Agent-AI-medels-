# command_create_thesis.py — create a thesis record (very short)
# command_create_thesis.py — ایجاد رکورد پایان‌نامه (خیلی کوتاه)

"""
Plain summary:
- Asks for student name, thesis title, and degree, then saves as 'draft'.

خلاصهٔ ساده:
- نام دانشجو، عنوان پایان‌نامه و مقطع را می‌پرسد و با وضعیت «پیش‌نویس» ذخیره می‌کند.

Dev note:
- Uses storage helpers to append a line to the data file.
- از توابع storage برای افزودن خط به فایل داده استفاده می‌کند.
"""

from thesis_management_system.thesis_data.storage import load_all_records, generate_new_id, append_record

def run():
    print("\nCreate a thesis record (ایجاد رکورد پایان‌نامه)\n")
    student_name = input("Student name (نام دانشجو): ").strip()
    thesis_title = input("Thesis title (عنوان پایان‌نامه): ").strip()
    degree = input("Degree (مثلاً MSc / BSc / PhD): ").strip()

    existing = load_all_records()
    new_id = generate_new_id(existing)
    record = {
        "id": new_id,
        "student_name": student_name or "(unknown)",
        "thesis_title": thesis_title or "(untitled)",
        "degree": degree or "(unknown)",
        "status": "draft",
    }
    append_record(record)
    print(f"\nSaved. New thesis id = {new_id} (ذخیره شد)\n")
