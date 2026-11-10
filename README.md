# 🎓 AcadTrack – Student Result Management System

AcadTrack is a Python-based student result management application developed using Streamlit and SQLite. It helps manage student academic records, calculate marks and grades, and retrieve results through a simple and interactive interface.

## 🚀 Features

- **Student Registration:** Enter student register number and name.
- **Marks Management:** Record marks for three subjects.
- **Automatic Calculations:** Calculate total marks and percentage.
- **Grade Calculation:** Generate grades automatically based on percentage.
- **Result Search:** Retrieve student results using register number.
- **Multiple Report Formats:** View Simple and Detailed student reports.
- **Student Records:** Display all saved student results.
- **Data Validation:** Validate required fields and restrict marks between 0 and 100.
- **Database Storage:** Store and retrieve academic records using SQLite.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and calculations |
| Streamlit | Interactive web interface |
| SQLite | Database management |
| HTML/CSS | Custom interface styling |
| GitHub | Source code management |

## 🧠 Object-Oriented Programming Concepts

This project demonstrates the following OOP concepts:

- **Class and Object:** The `Student` class represents student details and result calculations.
- **Inheritance:** `SimpleStudentReport` and `DetailedStudentReport` inherit from the `StudentReport` base class.
- **Abstraction:** The abstract `StudentReport` class defines the common `generate_report()` method.
- **Polymorphism:** Different report classes provide different outputs using the same method name.
- **Method Overriding:** Child classes provide their own implementation of `generate_report()`.

## 📊 Grade Calculation

The application calculates the percentage based on three subjects, each carrying 100 marks.

| Percentage | Grade |
|---|---|
| 90 and above | O |
| 80–89.99 | A+ |
| 70–79.99 | A |
| 60–69.99 | B+ |
| 50–59.99 | B |
| Below 50 | F |

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/diwakar533/student-result-management-system.git
```

### 2. Navigate to the Project Folder

```bash
cd student-result-management-system
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

### 5. Open in Browser

The application will run locally at:

```text
http://localhost:8501
```

## 🗄️ Database

SQLite is used to store student details, subject marks, total marks, percentages, and grades.

The database file `student_results.db` is automatically created when the application runs for the first time.

## 📁 Project Structure

```text
student-result-management-system/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 👨‍💻 Developer

**Diwakar Sathish**

B.Tech – Information Technology

St. Joseph's Institute of Technology, Chennai

**GitHub:** [diwakar533](https://github.com/diwakar533)

---

*AcadTrack – Making student result management simple, organized, and efficient.*
