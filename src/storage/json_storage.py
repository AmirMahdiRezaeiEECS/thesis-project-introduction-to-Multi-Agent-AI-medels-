"""
ماژول مدیریت فایل‌های JSON (json_storage.py)
هدف
ماژولی می‌سازیم که:

فایل‌های JSON (students.json, professors.json, courses.json, thesis.json, defended_thesis.json) رو بخونه و بنویسه.
عملیات پایه مثل اضافه کردن، به‌روزرسانی و حذف داده‌ها رو انجام بده.
قابل‌حمل (portable) باشه، یعنی از مسیرهای نسبی استفاده کنه.
خطاها (مثل نبود فایل) رو مدیریت کنه.
اصل Single Source of Truth رو رعایت کنه (هر داده فقط توی یه فایل JSON ذخیره بشه).

شبه‌کد (Pseudocode) : 

ماژول JsonStorage:
    ویژگی‌ها:
        مسیر_پوشه_داده (data_dir): مسیر نسبی پوشه data (مثل "data/")
    
    متد __init__:
        مسیر_پوشه_داده را تنظیم کن (پیش‌فرض: "data/")
        اطمینان بده که پوشه data وجود داره، اگه نه، بسازش

    متد read_json(نام_فایل):
        سعی کن فایل JSON رو از مسیر_پوشه_داده/نام_فایل بخونی
        اگه فایل وجود نداشت، یه لیست/دیکشنری خالی برگردون
        اگه خطایی رخ داد، خطا رو مدیریت کن و پیام مناسب برگردون
        داده JSON رو به‌عنوان لیست یا دیکشنری برگردون

    متد write_json(نام_فایل, داده):
        داده رو به‌عنوان JSON توی مسیر_پوشه_داده/نام_فایل بنویس
        از فرمت خوانا (indent=4) استفاده کن
        اگه خطایی رخ داد، خطا رو مدیریت کن و پیام مناسب برگردون

    متد update_json(نام_فایل, داده_جدید):
        داده فعلی رو از فایل بخون
        داده_جدید رو به داده فعلی اضافه کن یا به‌روزرسانی کن
        داده به‌روزرسانی‌شده رو توی فایل بنویس

    متد delete_from_json(نام_فایل, شرط_حذف):
        داده فعلی رو از فایل بخون
        داده‌هایی که شرط_حذف رو دارن حذف کن
        داده به‌روزرسانی‌شده رو توی فایل بنویس
"""



import json
import os

class JsonStorage:
    def __init__(self, data_dir="data"):
        """Initialize JsonStorage with a data directory."""
        self.data_dir = data_dir
        # Create data directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def read_json(self, filename):
        """Read data from a JSON file. Return empty list if file doesn't exist."""
        file_path = os.path.join(self.data_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return empty list if file doesn't exist
        except json.JSONDecodeError:
            print(f"Error: {filename} is not a valid JSON file.")
            return []
        except Exception as e:
            print(f"Error reading {filename}: {str(e)}")
            return []

    def write_json(self, filename, data):
        """Write data to a JSON file."""
        file_path = os.path.join(self.data_dir, filename)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error writing to {filename}: {str(e)}")
            return False

    def update_json(self, filename, new_data, key_field=None):
        """Update JSON file with new data. If key_field is provided, update by matching key."""
        current_data = self.read_json(filename)
        if not isinstance(current_data, list):
            current_data = [current_data]

        if key_field:
            # Update existing record if key_field matches
            for i, item in enumerate(current_data):
                if item.get(key_field) == new_data.get(key_field):
                    current_data[i] = new_data
                    break
            else:
                current_data.append(new_data)
        else:
            current_data.append(new_data)

        return self.write_json(filename, current_data)

    def delete_from_json(self, filename, condition):
        """Delete records from JSON file based on a condition function."""
        current_data = self.read_json(filename)
        if not isinstance(current_data, list):
            current_data = [current_data]

        # Keep only items that don't match the condition
        updated_data = [item for item in current_data if not condition(item)]
        return self.write_json(filename, updated_data)
    
    
    
    """
    
    توضیحات کد:

کلاس JsonStorage: یه کلاس شیءگرا برای مدیریت فایل‌های JSON.
__init__: مسیر پوشه data رو می‌گیره و اگه وجود نداشته باشه، می‌سازه.
read_json: فایل JSON رو می‌خونه. اگه فایل نباشه، یه لیست خالی برمی‌گردونه.
write_json: داده رو به‌صورت JSON ذخیره می‌کنه با فرمت خوانا (indent=4).
update_json: داده جدید رو اضافه یا به‌روزرسانی می‌کنه. اگه key_field داده بشه، بر اساس اون کلید (مثل student_code) داده رو به‌روزرسانی می‌کنه.
delete_from_json: داده‌هایی که یه شرط خاص (مثل تطبیق student_code) دارن رو حذف می‌کنه.
مدیریت خطا: خطاهایی مثل نبود فایل یا فرمت اشتباه JSON رو مدیریت می‌کنه.
قابلیت حمل: از os.path.join برای مسیرهای نسبی استفاده شده تا پروژه روی سیستم‌های مختلف کار کنه.

نکته آموزشی: توی این کد، ensure_ascii=False توی json.dump باعث می‌شه متن‌های غیرانگلیسی (مثل فارسی) درست ذخیره بشن. همچنین، encoding='utf-8' برای پشتیبانی از فارسی ضروریه.
    """