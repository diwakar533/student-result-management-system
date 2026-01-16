import streamlit as st

st.set_page_config(page_title="Student Result Management System")

st.title("🎓 Student Result Management System")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Select Option",
    ["Marks Entry", "View Result"]
)

# Function to calculate grade
def calculate_grade(percentage):
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
    else:
        return "F"

# Session state to store results
if "results" not in st.session_state:
    st.session_state.results = {}

# MARKS ENTRY PAGE
if menu == "Marks Entry":
    st.subheader("📝 Enter Student Marks")

    reg_no = st.text_input("Register Number")
    name = st.text_input("Student Name")

    mark1 = st.number_input("Subject 1 Marks", 0, 100)
    mark2 = st.number_input("Subject 2 Marks", 0, 100)
    mark3 = st.number_input("Subject 3 Marks", 0, 100)

    if st.button("Save Result"):
        total = mark1 + mark2 + mark3
        percentage = total / 3
        grade = calculate_grade(percentage)

        st.session_state.results[reg_no] = {
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        st.success("Result saved successfully!")

# VIEW RESULT PAGE
elif menu == "View Result":
    st.subheader("📄 View Student Result")

    search_reg = st.text_input("Enter Register Number")

    if st.button("View"):
        if search_reg in st.session_state.results:
            result = st.session_state.results[search_reg]

            st.write("**Student Name:**", result["name"])
            st.write("**Total Marks:**", result["total"])
            st.write("**Percentage:**", round(result["percentage"], 2))
            st.write("**Grade:**", result["grade"])
        else:
            st.error("Result not found!")
