# command_mark_submitted.py — mark a thesis as submitted
# command_mark_submitted.py — یک پایان‌نامه را به «ارسال‌شده» علامت بزن

"""
Plain summary:
- Ask for thesis id; if it's in draft, mark it submitted.

خلاصهٔ ساده:
- شناسهٔ پایان‌نامه را می‌گیرد؛ اگر در «پیش‌نویس» باشد، آن را «ارسال‌شده» می‌کند.

Dev note:
- Validates using core_logic.thesis_status before updating.
- با core_logic.thesis_status اعتبارسنجی می‌کند و بعد به‌روزرسانی می‌کند.
"""

from thesis_management_system.thesis_data.storage import load_all_records, update_record_status
from thesis_management_system.core_logic.thesis_status import DRAFT, SUBMITTED, is_valid_transition

def run():
    print("\nMark as submitted (علامت‌گذاری به ارسال‌شده)\n")
    thesis_id = input("Enter thesis id (شناسه): ").strip()
    records = load_all_records()
    target = next((r for r in records if r["id"] == thesis_id), None)
    if not target:
        print("\nNot found. (پیدا نشد.)\n")
        return
    current = target["status"]
    if not is_valid_transition(current, SUBMITTED):
        print(f"\nNot allowed from '{current}' to '{SUBMITTED}'. (مجاز نیست)\n")
        return
    if update_record_status(thesis_id, SUBMITTED):
        print("\nUpdated to 'submitted'. (به «ارسال‌شده» به‌روزرسانی شد)\n")
    else:
        print("\nUpdate failed. (به‌روزرسانی ناموفق)\n")
