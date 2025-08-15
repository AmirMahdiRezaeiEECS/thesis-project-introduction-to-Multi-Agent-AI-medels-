# storage.py — helper functions to read/write the text data file
# storage.py — توابع کمکی برای خواندن/نوشتن فایل متنی داده

"""
Plain summary:
- Saves and loads thesis records from a plain text file. Easy to read by humans.

خلاصهٔ ساده:
- رکوردهای پایان‌نامه را از یک فایل متنی ساده ذخیره/بارگذاری می‌کند. برای انسان قابل‌خواندن است.

Dev note:
- Format per line: id | student_name | thesis_title | degree | status
- Each function is small and focused (single responsibility).
- فرمت هر خط: id | نام دانشجو | عنوان پایان‌نامه | مقطع | وضعیت
- هر تابع کوچک و تک‌مسئولیتی است.
"""

from __future__ import annotations
from typing import List, Dict
from pathlib import Path

DATA_FILE = Path(__file__).parent / "thesis_records.txt"  # مسیر فایل داده

def ensure_data_file_exists() -> None:
    """Create the data file if it does not exist.
    اگر فایل داده وجود نداشته باشد، آن را بساز.
    """
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("", encoding="utf-8")  # create empty file

def parse_record_line(line: str) -> Dict[str, str] | None:
    """Parse one line into a record dict or return None if it's a comment/blank.
    یک خط را به دیکشنری رکورد تبدیل می‌کند؛ اگر خط خالی/کامنت باشد None برمی‌گرداند.
    """
    stripped = line.strip()
    if not stripped or stripped.startswith('#'):
        return None
    parts = [p.strip() for p in stripped.split('|')]
    if len(parts) != 5:
        return None
    return {
        "id": parts[0],
        "student_name": parts[1],
        "thesis_title": parts[2],
        "degree": parts[3],
        "status": parts[4],
    }

def format_record_line(record: Dict[str, str]) -> str:
    """Convert a record dict to a pipe-separated line.
    یک رکورد را به خط متنی با جداکننده '|' تبدیل می‌کند.
    """
    return f"{record['id']} | {record['student_name']} | {record['thesis_title']} | {record['degree']} | {record['status']}\n"

def load_all_records() -> List[Dict[str, str]]:
    """Load all records from the data file.
    همهٔ رکوردها را از فایل داده بارگذاری می‌کند.
    """
    ensure_data_file_exists()
    lines = DATA_FILE.read_text(encoding="utf-8").splitlines()
    out: List[Dict[str, str]] = []
    for ln in lines:
        rec = parse_record_line(ln)
        if rec:
            out.append(rec)
    return out

def generate_new_id(existing: List[Dict[str, str]]) -> str:
    """Return a new numeric id as string (max+1, starting from 1).
    یک شناسهٔ عددی جدید برمی‌گرداند (بیشینه+۱، شروع از ۱).
    """
    max_id = 0
    for rec in existing:
        try:
            max_id = max(max_id, int(rec["id"]))  # best-effort
        except Exception:
            continue
    return str(max_id + 1)

def append_record(record: Dict[str, str]) -> None:
    """Append a record to the data file.
    رکورد را به فایل داده اضافه می‌کند.
    """
    ensure_data_file_exists()
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(format_record_line(record))

def update_record_status(thesis_id: str, new_status: str) -> bool:
    """Update status for record with given id. Returns True if updated, else False.
    وضعیت رکورد با شناسهٔ داده‌شده را به‌روزرسانی می‌کند. اگر موفق بود True برمی‌گرداند.
    """
    ensure_data_file_exists()
    lines = DATA_FILE.read_text(encoding="utf-8").splitlines()
    updated = False
    new_lines = []
    for ln in lines:
        rec = parse_record_line(ln)
        if not rec:
            new_lines.append(ln)
            continue
        if rec["id"] == thesis_id:
            rec["status"] = new_status
            updated = True
            new_lines.append(format_record_line(rec).rstrip("\n"))
        else:
            new_lines.append(ln)
    DATA_FILE.write_text("\n".join(new_lines) + ("\n" if new_lines else ""), encoding="utf-8")
    return updated
