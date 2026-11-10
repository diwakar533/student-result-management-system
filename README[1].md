# AcadTrack – Student Result Management System

A Python-based student result management application built with Streamlit and SQLite.

## Features

- Enter student register number, name, and marks for three subjects.
- Calculate total marks, percentage, and grade automatically.
- Save student results in an SQLite database.
- Search for a student's result using their register number.
- Display Simple and Detailed report formats.
- View all saved student records.
- Validate required fields and restrict subject marks to 0–100.
- Update an existing record when the same register number is entered again.

## Technologies

- **Python** – application logic, calculations, and object-oriented design.
- **Streamlit** – interactive web interface.
- **SQLite** – persistent storage for student academic records.
- **HTML/CSS** – custom styling within the Streamlit interface.

## Object-Oriented Programming Concepts

- **Class and Object:** `Student` represents a student and calculates their result.
- **Inheritance:** `SimpleStudentReport` and `DetailedStudentReport` inherit from `StudentReport`.
- **Abstraction:** `StudentReport` defines the abstract `generate_report()` method.
- **Polymorphism and Method Overriding:** Both report classes provide their own implementation of `generate_report()`.

## Requirements

- Python 3.10 or later
- pip

## Run Locally

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Database

The application automatically creates `student_results.db` beside `app.py` when it first runs. The database stores saved results between local sessions. The database file is excluded from Git so student records are not accidentally committed.

## Grade Rules

The application calculates the average percentage across three subjects and assigns grades as follows:

| Percentage | Grade |
|---|---|
| 90 and above | O |
| 80–89.99 | A+ |
| 70–79.99 | A |
| 60–69.99 | B+ |
| 50–59.99 | B |
| Below 50 | F |

Adjust these rules if your institution follows a different grading scale.

## Note

This is an academic learning project. It does not include authentication or role-based access control. Do not use real or confidential student records in a public deployment.
