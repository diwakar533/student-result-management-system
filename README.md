# Student Result Management System

A Python web application built with Streamlit to enter student marks, calculate results, and save/retrieve student records using SQLite.

## Features

- Enter a student's register number and name.
- Enter marks for three subjects (each out of 100).
- Calculate total marks, percentage, and grade.
- Save records in an SQLite database.
- Search for a student's result by register number.
- Display a Simple Report or Detailed Report.
- View all saved student records.
- Validate required fields and restrict marks to the range 0–100.
- Use a custom UI colour palette inspired by yellow, blue, teal, red, and burgundy.

## Technologies

- Python
- Streamlit
- SQLite
- HTML/CSS (custom Streamlit styling)

## Object-Oriented Programming (OOP) concepts

- **Class and object:** `Student` represents a student and provides methods to calculate totals, percentages, grades, and record data.
- **Inheritance:** `SimpleStudentReport` and `DetailedStudentReport` inherit from `StudentReport`.
- **Abstraction:** `StudentReport` is an abstract base class with an abstract `generate_report()` method.
- **Polymorphism / method overriding:** Both report classes implement `generate_report()` differently. The app calls the same method on the selected report object and receives a different report format.

## Requirements

- Python 3.10 or later
- pip

## Run locally

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## Database

The app automatically creates `student_results.db` in the same folder as `app.py` when it first runs. The database stores saved student results between app sessions. Keep this file if you want to retain your local records. The database file is excluded from Git by `.gitignore` so personal/student records are not accidentally uploaded.

## Grade rules

The current grade rules are defined in `Student.calculate_grade()`:

- 90% and above: O
- 80–89.99%: A+
- 70–79.99%: A
- 60–69.99%: B+
- 50–59.99%: B
- Below 50%: F

Adjust these rules if your institution uses a different grading scale.

## Limitations

This is a learning project. It does not include authentication, role-based permissions, or production-grade security. Do not upload real student data or secrets to a public repository.
