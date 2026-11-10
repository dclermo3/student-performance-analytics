# Student Performance Analytics Dashboard

An interactive data analytics dashboard built with **Python, Pandas, SQLite, Plotly, and Streamlit** to explore student academic performance and identify trends in grades, study habits, and school attendance.

**[View Live Dashboard](https://student-performance-analytics-data.streamlit.app/)** | **[GitHub Repository](https://github.com/dclermo3/student-performance-analytics)**

## Project Overview

This project analyzes real-world student performance data to explore how study habits and attendance relate to academic achievement.

Using Python for data analysis, SQLite for database management, and Streamlit for interactive visualization, I developed a dashboard that allows users to explore academic performance trends and filter student data.

The project demonstrates practical skills in data processing, SQL, exploratory data analysis, data visualization, and web application development.

## Dataset

This project uses the **Student Performance Dataset** from the UCI Machine Learning Repository.

**Original source:** [UCI Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student+performance)

The dataset contains student achievement information collected from two Portuguese secondary schools.

### Dataset Information

| Category | Details |
|---|---|
| Dataset | Student Performance |
| Source | UCI Machine Learning Repository |
| File analyzed | `student-mat.csv` |
| Subject | Mathematics |
| Number of students | 395 |
| Number of attributes | 33 |
| Location | Portugal |
| Final grade scale | 0–20 |

The dataset contains information about students' academic performance, demographics, family backgrounds, study habits, and school attendance.

### Variables Used in the Analysis

| Variable | Description |
|---|---|
| `G3` | Final mathematics grade (0–20) |
| `studytime` | Weekly study-time category (1–4) |
| `absences` | Number of school absences |
| `school` | School attended |

The `studytime` variable is categorical:

- 1 = Less than 2 hours per week
- 2 = 2–5 hours per week
- 3 = 5–10 hours per week
- 4 = More than 10 hours per week

The analysis focuses on the mathematics dataset rather than combining mathematics and Portuguese language records.

**Dataset reference:** Cortez, P., & Silva, A. (2008). *Using Data Mining to Predict Secondary School Student Performance.*

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and application development |
| Pandas | Data manipulation and statistical analysis |
| SQLite | Database creation, storage, and SQL queries |
| Plotly | Interactive data visualizations |
| Streamlit | Interactive web dashboard |
| Matplotlib | Exploratory data visualization |
| Git & GitHub | Version control and source code hosting |

## Dashboard Features

The interactive dashboard includes:

- **Student Overview:** Total students, average final grade, pass count, fail count, and pass rate.
- **Grade Distribution:** Visualization of students' final mathematics grades.
- **Study Time Analysis:** Comparison of average final grades across study-time categories.
- **Attendance Analysis:** Scatter plot exploring the relationship between absences and final grades.
- **Interactive Filters:** Filter student records by school and study-time category.
- **Key Insights:** Summary of important findings from the analysis.

## Key Findings

The analysis of 395 mathematics students produced the following results:

| Metric | Result |
|---|---|
| Total Students | 395 |
| Average Final Grade | 10.42 / 20 |
| Highest Final Grade | 20 / 20 |
| Lowest Final Grade | 0 / 20 |
| Students Passed | 265 |
| Students Failed | 130 |
| Overall Pass Rate | 67.1% |

A passing grade was defined as a final mathematics grade of at least 10 out of 20.

### Study Time and Academic Performance

Average final grades by weekly study-time category:

| Study Time | Average Final Grade |
|---|---|
| Less than 2 hours | 10.05 |
| 2–5 hours | 10.17 |
| 5–10 hours | 11.40 |
| More than 10 hours | 11.26 |

Students in the higher study-time categories generally achieved slightly higher average grades, although the relationship was not perfectly linear.

### Absences and Final Grades

The Pearson correlation between absences and final grades was approximately **0.034**.

This indicates almost no linear relationship between absences and final grades in this dataset.

These results describe patterns and associations within the data, not proof of cause and effect.

## Project Structure

```text
student-performance-analytics/
├── app.py
├── analysis.py
├── database.py
├── data/
│   └── student-mat.csv
├── database/
├── requirements.txt
├── README.md
├── .gitignore
├── grade_distribution.png
├── study_time_analysis.png
└── absences_analysis.png
```

### Main Files

- `app.py` — Streamlit dashboard and interactive visualizations
- `analysis.py` — Exploratory data analysis using Pandas and Matplotlib
- `database.py` — SQLite database creation and SQL analysis
- `data/student-mat.csv` — Student mathematics performance dataset
- `requirements.txt` — Python dependencies

## How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://