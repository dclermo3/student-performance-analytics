import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Page configuration
st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide"
)

# Connect to database
from pathlib import Path

db_path = Path("database/students.db")

if not db_path.exists():
    import database
connection = sqlite3.connect("database/students.db")

students = pd.read_sql_query(
    "SELECT * FROM students",
    connection
)

connection.close()
# Sidebar filters
st.sidebar.header("Dashboard Filters")

# School filter
selected_schools = st.sidebar.multiselect(
    "Select School",
    options=sorted(students["school"].unique()),
    default=sorted(students["school"].unique())
)

# Study time filter
selected_studytime = st.sidebar.multiselect(
    "Select Study Time",
    options=sorted(students["studytime"].unique()),
    default=sorted(students["studytime"].unique())
)

# Apply filters
students = students[
    (students["school"].isin(selected_schools)) &
    (students["studytime"].isin(selected_studytime))
]
# Stop if no students match the filters
if students.empty:
    st.warning("No students match your filters. Please select another option.")
    st.stop()
# Dashboard title
st.title("🎓 Student Performance Analytics Dashboard")

st.write("Explore student grades, study habits, and academic performance.")

# Dashboard metrics
total_students = len(students)
average_grade = students["G3"].mean()
passed = (students["G3"] >= 10).sum()
failed = (students["G3"] < 10).sum()
pass_rate = (passed / total_students * 100) if total_students > 0 else 0
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Students", total_students)
col2.metric("Average Grade", round(average_grade, 2))
col3.metric("Passed", passed)
col4.metric("Failed", failed)
col5.metric("Pass Rate", f"{pass_rate:.1f}%")

# Grade distribution
st.subheader("Final Grade Distribution")

fig = px.histogram(
    students,
    x="G3",
    nbins=21,
    title="Distribution of Final Grades",
    labels={"G3": "Final Grade"}
)

st.plotly_chart(fig, width="stretch")

# Study time analysis
st.subheader("Study Time vs Average Grade")

study_data = students.groupby("studytime", as_index=False)["G3"].mean()
# Convert study time numbers into readable labels
study_labels = {
    1: "Less than 2 hours",
    2: "2-5 hours",
    3: "5-10 hours",
    4: "More than 10 hours"
}

study_data["studytime_label"] = study_data["studytime"].map(study_labels)
fig2 = px.bar(
    study_data,
    x="studytime_label",
    y="G3",
    title="Average Final Grade by Weekly Study Time",
    labels={
        "studytime_label": "Weekly Study Time",
        "G3": "Average Final Grade"
    },
    color="G3",
    color_continuous_scale="Blues"
)

fig2.update_layout(
    xaxis_categoryorder="array",
    xaxis_categoryarray=[
        "Less than 2 hours",
        "2-5 hours",
        "5-10 hours",
        "More than 10 hours"
    ]
)

st.plotly_chart(fig2, width="stretch")

# Absences analysis
st.subheader("Absences vs Final Grades")

fig3 = px.scatter(
    students,
    x="absences",
    y="G3",
    title="Relationship Between Absences and Final Grades",
    labels={
        "absences": "Number of Absences",
        "G3": "Final Grade"
    }
)

st.plotly_chart(fig3, width="stretch")

# Key insights section
st.divider()

st.subheader("📊 Key Insights")

st.write(
    "This dashboard analyzes student academic performance "
    "using data from 395 students across two schools."
)

# Calculate insights from the currently filtered students
if not students.empty:
    best_studytime = students.groupby("studytime")["G3"].mean().idxmax()

    study_labels = {
        1: "Less than 2 hours",
        2: "2-5 hours",
        3: "5-10 hours",
        4: "More than 10 hours"
    }

    st.success(
        f"Highest Average Grade: Students studying "
        f"{study_labels[best_studytime]} per week had the "
        f"highest average final grade in the selected data."
    )

    correlation = students["absences"].corr(students["G3"])

    if pd.notna(correlation):
        st.info(
            f"Absences and Final Grades Correlation: {correlation:.3f}. "
            "This measures the linear relationship between absences "
            "and academic performance."
        )

    st.write(
        f"Pass Rate: {pass_rate:.1f}% of students in the "
        f"selected data achieved a passing grade of 10 or higher."
    )
else:
    st.warning("No students match the selected filters.")