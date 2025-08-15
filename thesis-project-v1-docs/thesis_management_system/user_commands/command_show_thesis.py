# command_show_thesis.py — show all thesis records (very short)
# command_show_thesis.py — نمایش همهٔ رکوردهای پایان‌نامه (خیلی کوتاه)

"""
Plain summary:
- Prints all saved thesis records and their statuses.

خلاصهٔ ساده:
- همهٔ رکوردهای ذخیره‌شده و وضعیت آن‌ها را چاپ می‌کند.

Dev note:
- Reads the data file and prints a simple table.
- فایل داده را می‌خواند و یک جدول ساده چاپ می‌کند.
"""

from thesis_management_system.thesis_data.storage import load_all_records

def run():
    records = load_all_records()
    if not records:
        print("\nNo records yet. (هنوز رکوردی وجود ندارد.)\n")
        return
    print("\nAll thesis records (همهٔ رکوردها):\n")
    print("ID | Student | Title | Degree | Status")
    print("-- | ------- | ----- | ------ | ------")
    for r in records:
        print(f"{r['id']} | {r['student_name']} | {r['thesis_title']} | {r['degree']} | {r['status']}")
    print()
