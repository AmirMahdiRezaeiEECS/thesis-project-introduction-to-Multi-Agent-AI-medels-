# thesis_status.py — holds simple thesis statuses and a checker
# thesis_status.py — وضعیت‌های سادهٔ پایان‌نامه و تابع بررسی را نگه می‌دارد

"""
Plain summary:
- Lists statuses (draft, submitted) and a small function to check transitions.

خلاصهٔ ساده:
- وضعیت‌ها را فهرست می‌کند (پیش‌نویس، ارسال‌شده) و یک تابع کوچک برای بررسی تغییر وضعیت دارد.

Dev note:
- Exposes is_valid_transition(current_status, next_status) -> bool.
- تابع is_valid_transition(current_status, next_status) -> bool را ارائه می‌دهد.
"""

# We keep names simple and lowercase so non-programmers can read them easily.
# نام‌ها ساده و با حروف کوچک نگه داشته شده تا برای غیرمتخصص هم خوانا باشد.

DRAFT = "draft"            # پیش‌نویس
SUBMITTED = "submitted"    # ارسال‌شده

ALL_STATUSES = {DRAFT, SUBMITTED}

def is_valid_transition(current_status: str, next_status: str) -> bool:
    """Return True if moving from current_status to next_status is allowed in v1.

    در نسخه ۱ اگر گذار از پیش‌نویس به ارسال‌شده باشد، مجاز است. برگشت نداریم.
    """
    if current_status not in ALL_STATUSES or next_status not in ALL_STATUSES:
        return False
    # In v1, the only forward move is draft -> submitted.
    # در نسخه ۱ تنها حرکت مجاز: پیش‌نویس -> ارسال‌شده.
    return (current_status == DRAFT and next_status == SUBMITTED)
