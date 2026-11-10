import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path

import streamlit as st

# Store the database beside this application file.
DB_PATH = Path(__file__).with_name("student_results.db")


# -------------------- OOP: Student class --------------------
class Student:
    """Represents a student and calculates the student's result."""

    def __init__(self, register_number, name, mark1, mark2, mark3):
        self.register_number = register_number.strip()
        self.name = name.strip()
        self.marks = [int(mark1), int(mark2), int(mark3)]

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        # Three subjects, each out of 100.
        return self.calculate_total() / 3

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "O"
        elif percentage >= 80:
            return "A+"
        elif percentage >= 70:
            return "A"
        elif percentage >= 60:
            return "B+"
        elif percentage >= 50:
            return "B"
        return "F"

    def to_record(self):
        return {
            "register_number": self.register_number,
            "name": self.name,
            "mark1": self.marks[0],
            "mark2": self.marks[1],
            "mark3": self.marks[2],
            "total": self.calculate_total(),
            "percentage": self.calculate_percentage(),
            "grade": self.calculate_grade(),
        }


# -------------------- OOP: Inheritance and polymorphism --------------------
class StudentReport(ABC):
    """Base class for different report formats."""

    @abstractmethod
    def generate_report(self, student_record):
        """Return report content for a student."""
        raise NotImplementedError


class SimpleStudentReport(StudentReport):
    def generate_report(self, student_record):
        # Overridden method: simple report format.
        return {
            "Student Name": student_record["name"],
            "Percentage": f'{student_record["percentage"]:.2f}%',
            "Grade": student_record["grade"],
        }


class DetailedStudentReport(StudentReport):
    def generate_report(self, student_record):
        # Overridden method: detailed report format.
        return {
            "Register Number": student_record["register_number"],
            "Student Name": student_record["name"],
            "Subject 1 Marks": student_record["mark1"],
            "Subject 2 Marks": student_record["mark2"],
            "Subject 3 Marks": student_record["mark3"],
            "Total Marks": f'{student_record["total"]}/300',
            "Percentage": f'{student_record["percentage"]:.2f}%',
            "Grade": student_record["grade"],
        }


# -------------------- Database functions --------------------
def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS student_results (
                register_number TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                mark1 INTEGER NOT NULL CHECK(mark1 BETWEEN 0 AND 100),
                mark2 INTEGER NOT NULL CHECK(mark2 BETWEEN 0 AND 100),
                mark3 INTEGER NOT NULL CHECK(mark3 BETWEEN 0 AND 100),
                total INTEGER NOT NULL,
                percentage REAL NOT NULL,
                grade TEXT NOT NULL
            )
            """
        )


def save_student(student_record):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO student_results
            (register_number, name, mark1, mark2, mark3, total, percentage, grade)
            VALUES (:register_number, :name, :mark1, :mark2, :mark3, :total, :percentage, :grade)
            ON CONFLICT(register_number) DO UPDATE SET
                name = excluded.name,
                mark1 = excluded.mark1,
                mark2 = excluded.mark2,
                mark3 = excluded.mark3,
                total = excluded.total,
                percentage = excluded.percentage,
                grade = excluded.grade
            """,
            student_record,
        )


def find_student(register_number):
    with get_connection() as connection:
        connection.row_factory = sqlite3.Row
        row = connection.execute(
            "SELECT * FROM student_results WHERE register_number = ?",
            (register_number.strip(),),
        ).fetchone()
        return dict(row) if row else None


def get_all_students():
    with get_connection() as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT * FROM student_results ORDER BY register_number"
        ).fetchall()
        return [dict(row) for row in rows]


# -------------------- Streamlit user interface --------------------
st.set_page_config(page_title="Student Result Management System", page_icon="🎓", layout="centered")

# Custom UI palette inspired by the user's reference image:
# yellow, blue, teal, bright red, and burgundy.
st.markdown(
    """
    <style>
    :root {
        --palette-yellow: #F5D900;
        --palette-blue: #0877D1;
        --palette-teal: #009B87;
        --palette-red: #F2342B;
        --palette-burgundy: #85123D;
        --ink: #25233A;
        --paper: #FFFDF8;
    }

    .stApp {
        background: linear-gradient(145deg, #FFFDF8 0%, #F4F8FC 58%, #FFF5F2 100%);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: rgba(255, 253, 248, 0.92);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0877D1 0%, #009B87 48%, #85123D 100%);
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: rgba(255,255,255,0.14);
        border-color: rgba(255,255,255,0.45);
    }

    h1, h2, h3 { color: var(--palette-burgundy) !important; }
    p, label, [data-testid="stMarkdownContainer"] { color: var(--ink); }
    h1 { border-bottom: 5px solid var(--palette-yellow); padding-bottom: 0.45rem; }

    [data-testid="stForm"], [data-testid="stDataFrame"],
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px;
    }

    [data-testid="stForm"] {
        background: rgba(255,255,255,0.88);
        border: 1px solid #D9E5EF;
        padding: 1.1rem;
        box-shadow: 0 8px 24px rgba(8, 54, 91, 0.08);
    }

    div[data-testid="stButton"] > button,
    div[data-testid="stFormSubmitButton"] > button {
        background: var(--palette-blue);
        color: #FFFFFF;
        border: 0;
        border-radius: 10px;
        font-weight: 700;
        transition: all 0.18s ease;
    }
    div[data-testid="stButton"] > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: var(--palette-burgundy);
        color: #FFFFFF;
        border: 0;
        box-shadow: 0 4px 12px rgba(133, 18, 61, 0.2);
    }

    input, textarea, [data-baseweb="select"] > div,
    [data-testid="stNumberInput"] button {
        border-radius: 9px !important;
    }
    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input {
        background: #FFFFFF;
        color: var(--ink);
    }

    [data-testid="stAlert"] { border-radius: 12px; }
    [data-testid="stAlert"] [data-testid="stMarkdownContainer"] p { color: inherit; }

    [data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {
        border-color: var(--palette-teal);
    }
    [data-testid="stRadio"] label[data-baseweb="radio"] input:checked + div {
        background-color: var(--palette-teal);
    }

    [data-testid="stDataFrame"] {
        border-top: 4px solid var(--palette-yellow);
        border-radius: 12px;
        overflow: hidden;
    }

    /* Small multicolour accent inspired by the reference palette. */
    .palette-accent {
        height: 7px;
        border-radius: 99px;
        margin: 0.4rem 0 1.2rem 0;
        background: linear-gradient(90deg,
            var(--palette-yellow) 0 20%,
            var(--palette-blue) 20% 40%,
            var(--palette-teal) 40% 60%,
            var(--palette-red) 60% 80%,
            var(--palette-burgundy) 80% 100%);
    }
    </style>
    <div class="palette-accent"></div>
    """,
    unsafe_allow_html=True,
)
initialize_database()

st.title("🎓 Student Result Management System")
st.caption("Manage student marks, calculate grades, and retrieve saved results.")

menu = st.sidebar.selectbox("Select Option", ["Marks Entry", "View Result", "All Students"])

if menu == "Marks Entry":
    st.subheader("📝 Enter Student Marks")
    st.info("Saving another result with the same register number updates that student's record.")

    with st.form("marks_entry_form"):
        reg_no = st.text_input("Register Number")
        name = st.text_input("Student Name")
        col1, col2, col3 = st.columns(3)
        with col1:
            mark1 = st.number_input("Subject 1", min_value=0, max_value=100, step=1)
        with col2:
            mark2 = st.number_input("Subject 2", min_value=0, max_value=100, step=1)
        with col3:
            mark3 = st.number_input("Subject 3", min_value=0, max_value=100, step=1)
        submitted = st.form_submit_button("Save Result", type="primary")

    if submitted:
        if not reg_no.strip() or not name.strip():
            st.error("Please enter both the register number and student name.")
        else:
            student = Student(reg_no, name, mark1, mark2, mark3)
            record = student.to_record()
            save_student(record)
            st.success("Student result saved successfully in the database!")
            st.write(f"**Total:** {record['total']}/300")
            st.write(f"**Percentage:** {record['percentage']:.2f}%")
            st.write(f"**Grade:** {record['grade']}")

elif menu == "View Result":
    st.subheader("📄 View Student Result")
    search_reg = st.text_input("Enter Register Number")
    report_type = st.radio("Report Format", ["Simple Report", "Detailed Report"], horizontal=True)

    if st.button("View Result", type="primary"):
        if not search_reg.strip():
            st.warning("Please enter a register number.")
        else:
            record = find_student(search_reg)
            if record:
                report_generator = (
                    SimpleStudentReport()
                    if report_type == "Simple Report"
                    else DetailedStudentReport()
                )
                report = report_generator.generate_report(record)
                st.success("Student result found.")
                for label, value in report.items():
                    st.write(f"**{label}:** {value}")
            else:
                st.error("Result not found. Please check the register number.")

else:
    st.subheader("👥 All Student Results")
    records = get_all_students()
    if records:
        st.dataframe(
            [
                {
                    "Register Number": r["register_number"],
                    "Student Name": r["name"],
                    "Total / 300": r["total"],
                    "Percentage": round(r["percentage"], 2),
                    "Grade": r["grade"],
                }
                for r in records
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No student records have been saved yet.")
