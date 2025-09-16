Thesis Management System
This is a Minimum Viable Product (MVP) for a Thesis Management System implemented in Python. It allows students and professors to manage thesis-related processes such as course selection, thesis requests, defense requests, and searching defended theses.
Features

User Roles: Supports two roles: Student and Professor.
Student Features:
View available courses.
Submit thesis requests (auto-approved in MVP).
Submit defense requests with title, keywords, and PDF path.
Search defended theses by title, author, or keywords.


Professor Features:
View thesis requests.
Manage defense requests (approve/reject, set date and judges).
Search defended theses.


Data Storage: Uses JSON files for data persistence (students.json, professors.json, courses.json, thesis.json, defended_thesis.json).
CLI Interface: Simple command-line interface for user interaction.

Project Structure
thesis_management_system/
├── data/
│   ├── students.json
│   ├── professors.json
│   ├── courses.json
│   ├── thesis.json
│   ├── defended_thesis.json
│   ├── uploads/
├── src/
│   ├── entities/
│   │   ├── user.py
│   │   ├── student.py
│   │   ├── professor.py
│   │   ├── course.py
│   │   ├── thesis.py
│   │   ├── defense.py
│   ├── interfaces/
│   │   ├── auth.py
│   │   ├── welcome.py
│   │   ├── student_menu.py
│   │   ├── professor_menu.py
│   ├── storage/
│   │   ├── json_storage.py
├── tests/
│   ├── test_json_storage.py
│   ├── test_auth.py
│   ├── test_entities.py
│   ├── test_menus.py
│   ├── test_main.py
│   ├── test_comprehensive.py
├── main_program.py
├── README.md

Setup

Ensure Python 3.11+ is installed.
Clone or download the project.
Create the data/ directory with sample JSON files (provided in the project).
Create the data/uploads/ directory for storing PDF file paths (no real files needed for MVP).
Install pytest for running tests:pip install pytest



Running the Program

Run the main program:python main_program.py


Login as a student (code: 0000, password: 0000) or professor (code: 1111, password: 1111).
Use the CLI menu to interact with the system.

Running Tests
Run all tests with:
pytest -s

Or run a specific test, e.g.:
pytest tests/test_comprehensive.py -s

Future Improvements

Add real PDF file handling.
Implement capacity restrictions for courses and professors.
Enhance search functionality with more filters.
Add validation for user inputs (e.g., date format, file existence).
Support for multiple semesters and years.

Notes

The system uses relative paths for portability.
Data is stored in JSON files to follow the Single Source of Truth principle.
The MVP auto-approves thesis requests for simplicity.
