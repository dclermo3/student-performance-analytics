import pandas as pd
import matplotlib.pyplot as plt

# Load student dataset
students = pd.read_csv("data/student-mat.csv", sep=";")

# Display first 5 students
print(students.head())

# Display dataset information
print(students.info())

# Display average final grade
print("Average Final Grade:", students["G3"].mean())

# Student grade statistics

print("Highest Grade:", students["G3"].max())

print("Lowest Grade:", students["G3"].min())

print("Students Passed:", (students["G3"] >= 10).sum())

print("Students Failed:", (students["G3"] < 10).sum())

# Create a graph of student final grades

plt.figure(figsize=(10, 6))

plt.hist(students["G3"], bins=20, color="skyblue", edgecolor="black")

plt.title("Student Final Grade Distribution")
plt.xlabel("Final Grade (0-20)")
plt.ylabel("Number of Students")

plt.grid(axis="y", alpha=0.3)

plt.savefig("grade_distribution.png")

plt.show()

# Analyze average grades by study time

study_analysis = students.groupby("studytime")["G3"].mean()

print("\nAverage Final Grade by Study Time:")
print(study_analysis)

# Create study time comparison graph

plt.figure(figsize=(9, 5))

study_analysis.plot(kind="bar", color="mediumseagreen", edgecolor="black")

plt.title("Average Final Grade by Weekly Study Time")
plt.xlabel("Study Time Category")
plt.ylabel("Average Final Grade (0-20)")

plt.xticks(rotation=0)
plt.ylim(0, 20)
plt.tight_layout()

plt.savefig("study_time_analysis.png")
plt.show()

# Analyze relationship between absences and final grades

correlation = students["absences"].corr(students["G3"])

print("\nCorrelation Between Absences and Final Grades:")
print(round(correlation, 3))

# Create scatter plot

plt.figure(figsize=(9, 5))

plt.scatter(
    students["absences"],
    students["G3"],
    color="royalblue",
    alpha=0.5
)

plt.title("Student Absences vs Final Grades")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (0-20)")

plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("absences_analysis.png")
plt.show()