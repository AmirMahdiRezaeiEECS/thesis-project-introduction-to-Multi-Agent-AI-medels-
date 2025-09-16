شبه کد : 

کلاس User (پایه):
    ویژگی‌ها:
        name: نام کاربر
        code: کد کاربر (student_code یا teacher_code)
        password: رمز عبور
    متد __init__(داده):
        تنظیم name، code و password از داده JSON

کلاس Student (ارث‌بری از User):
    متد __init__(داده):
        فراخوانی __init__ کلاس پایه با student_code به‌عنوان code
    متد view_courses:
        خواندن courses.json
        نمایش درس‌های با ظرفیت غیرصفر
    متد submit_thesis_request(course_id):
        چک کردن وجود درس و ظرفیت
        ثبت درخواست در thesis.json (با status="approved" در MVP)
    متد submit_defense_request(title, keywords, pdf_path):
        اعتبارسنجی pdf_path
        ثبت در defended_thesis.json
        به‌روزرسانی thesis.json (status="defending")
    متد search_theses(search_term):
        جست‌وجو در defended_thesis.json بر اساس title، keywords، name
        نمایش نتایج

کلاس Professor (ارث‌بری از User):
    متد __init__(داده):
        فراخوانی __init__ کلاس پایه با teacher_code به‌عنوان code
    متد view_thesis_requests:
        خواندن thesis.json و نمایش درخواست‌های مرتبط با استاد
        در MVP: همه درخواست‌ها به‌صورت mocked نمایش داده می‌شن
    متد manage_defense_requests:
        خواندن defended_thesis.json
        انتخاب درخواست، تأیید/رد، تنظیم defense_date و judges
        به‌روزرسانی thesis.json و defended_thesis.json
    متد search_theses(search_term):
        مشابه Student.search_theses

کلاس Course:
    ویژگی‌ها:
        course_id, title, professor_code, year, semester, capacity, resources, sessions, unit
    متد __init__(داده):
        تنظیم ویژگی‌ها از داده JSON
    متد has_capacity:
        چک کردن capacity > 0
        بازگشت True/False

کلاس Thesis:
    ویژگی‌ها:
        student_code, course_id, request_date, status, approval_date, defense_date, files, score, judges
    متد __init__(داده):
        تنظیم ویژگی‌ها از داده JSON
    متد submit:
        ذخیره در thesis.json
    متد update_status(status, defense_date, judges):
        به‌روزرسانی status، defense_date و judges در thesis.json

کلاس Defense:
    ویژگی‌ها:
        student_code, course_id, title, year, semester, supervisor, judges, score, files, keywords
    متد __init__(داده):
        تنظیم ویژگی‌ها از داده JSON
    متد submit:
        ذخیره در defended_thesis.json
    متد assign_score(score):
        به‌روزرسانی score در defended_thesis.json