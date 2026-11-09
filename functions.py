"""Reusable calculations and analysis functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Statistics", "AI_Basics"]
PASS_MARK = 35

def validate_dataset(data):
    """Check required columns and basic data validity."""
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percent"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing)}")
    if data.empty:
        raise ValueError("The dataset contains no student records.")
    for subject in SUBJECTS:
        data[subject] = pd.to_numeric(data[subject], errors="raise")
        if not data[subject].between(0, 100).all():
            raise ValueError(f"{subject} marks must be between 0 and 100.")
    data["Attendance_Percent"] = pd.to_numeric(data["Attendance_Percent"], errors="raise")
    if not data["Attendance_Percent"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")
    return data

def calculate_student_results(data):
    """Add total, average, grade and pass/fail columns."""
    result = data.copy()
    marks = result[SUBJECTS].to_numpy(dtype=float)
    result["Total_Marks"] = np.sum(marks, axis=1)
    result["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)

    def assign_grade(average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    result["Grade"] = result["Average_Marks"].apply(assign_grade)
    # A student passes only when every subject mark is at least PASS_MARK.
    result["Result"] = np.where((result[SUBJECTS] >= PASS_MARK).all(axis=1), "Pass", "Fail")
    return result

def get_subject_summary(data):
    """Return average, highest and lowest marks for every subject."""
    summary = []
    for subject in SUBJECTS:  # Loop through subjects as required by the assignment.
        summary.append({
            "Subject": subject,
            "Average": round(float(np.mean(data[subject].to_numpy())), 2),
            "Highest": int(data[subject].max()),
            "Lowest": int(data[subject].min())
        })
    return pd.DataFrame(summary)

def get_class_summary(results):
    """Calculate overall class statistics."""
    return {
        "Students": len(results),
        "Passed": int((results["Result"] == "Pass").sum()),
        "Failed": int((results["Result"] == "Fail").sum()),
        "Pass_Percentage": round((results["Result"] == "Pass").mean() * 100, 2),
        "Class_Average": round(float(results["Average_Marks"].mean()), 2),
        "Highest_Average": round(float(results["Average_Marks"].max()), 2),
        "Lowest_Average": round(float(results["Average_Marks"].min()), 2),
    }
