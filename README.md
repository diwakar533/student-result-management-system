# Student Result Management System

A Python-based Student Result Management System developed using Streamlit. The application allows users to enter student details, calculate marks and grades, store results in an SQLite database, and retrieve student reports through a simple web interface.

## Features

- **Student Details:** Enter the register number and student name.
- **Marks Management:** Enter marks for three subjects.
- **Automatic Calculation:** Calculate total marks and percentage.
- **Grade Calculation:** Assign grades based on percentage.
- **Database Integration:** Store and retrieve student results using SQLite.
- **Result Search:** Find student results using the register number.
- **Multiple Report Formats:** Generate simple and detailed student reports.
- **Input Validation:** Validate student information and marks.
- **User Interface:** Custom CSS styling with a yellow, blue, teal, red, and burgundy colour palette.

## Technologies Used

- Python
- Streamlit
- SQLite
- Object-Oriented Programming (OOP)
- HTML and CSS styling through Streamlit

## Object-Oriented Programming Concepts

### 1. Classes and Objects
The `Student` class organizes student information and result-related operations.

### 2. Encapsulation
Student data and related methods are organized within classes to improve code structure.

### 3. Inheritance
The `SimpleStudentReport` and `DetailedStudentReport` classes inherit from the common `StudentReport` base class.

### 4. Polymorphism
Both report classes implement the `generate_report()` method differently. The same method call can generate different report formats depending on the object.

### 5. Abstraction
The abstract `StudentReport` class defines a common interface for report generation.

## Installation and Setup

### Prerequisites
- Python installed on your computer
- Visual Studio Code or another Python editor

### Step 1: Clone the Repository

```bash
git clone https://github.com/diwakar533/student-result-management-system.git
```

### Step 2: Open the Project Folder

```bash
cd student-result-management-system
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## How to Use

1. Open the application.
2. Select **Marks Entry** from the sidebar.
3. Enter the student's register number and name.
4. Enter the marks for the three subjects.
5. Click **Save Result**.
6. Select **View Result** to retrieve the saved record.
7. Choose Simple Report or Detailed Report to view the result in the desired format.

## Example

| Subject | Marks |
|---|---:|
| Subject 1 | 50 |
| Subject 2 | 60 |
| Subject 3 | 70 |
| **Total** | **180/300** |
| **Percentage** | **60%** |
| **Grade** | **B+** |

*The grade depends on the grading rules configured in the application.*

## Database

The application uses SQLite to store student results. Records can be retrieved after refreshing or restarting the application, provided the same database file is retained.

## Future Enhancements

- Support for more subjects.
- Student login and authentication.
- Export student reports as PDF.
- Admin dashboard and result analytics.
- Improved database management and report generation.

## Learning Outcomes

Through this project, I gained practical experience in Python programming, Streamlit application development, database integration, input validation, and object-oriented programming concepts such as inheritance, abstraction, and polymorphism.

## Author

**Diwakar Sathish**

B.Tech Information Technology Student

GitHub: [diwakar533](https://github.com/diwakar533)

---

If you find this project useful, feel free to explore the repository and share your feedback.
