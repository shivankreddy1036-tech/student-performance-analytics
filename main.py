"""Student Performance Analytics System
Run with: python main.py
Dataset values are synthetic sample data created for demonstration.
"""

from pathlib import Path
import pandas as pd
from functions import (
    SUBJECTS, validate_dataset, calculate_student_results,
    get_subject_summary, get_class_summary
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "students.csv"
OUTPUT_DIR = BASE_DIR / "output"

def display_heading(title):
    print("\n" + "=" * 72)
    print(title.center(72))
    print("=" * 72)

def main():
    try:
        # Step 1: Load and validate data using Pandas.
        data = pd.read_csv(DATA_FILE)
        data = validate_dataset(data)

        # Step 2: Calculate student-wise results.
        results = calculate_student_results(data)

        # Step 3: Display records and summary.
        display_heading("STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print(f"Total student records: {len(results)}")
        print("\nSTUDENT-WISE RESULTS")
        columns = ["Student_ID", "Name", "Department", "Total_Marks",
                   "Average_Marks", "Grade", "Result", "Attendance_Percent"]
        print(results[columns].to_string(index=False))

        summary = get_class_summary(results)
        display_heading("OVERALL CLASS SUMMARY")
        for label, value in summary.items():
            print(f"{label.replace('_', ' '):25}: {value}")

        # Step 4: Subject-wise analysis.
        display_heading("SUBJECT-WISE PERFORMANCE")
        subject_summary = get_subject_summary(data)
        print(subject_summary.to_string(index=False))

        # Step 5: Identify top performers.
        display_heading("TOP 5 PERFORMING STUDENTS")
        top_students = results.nlargest(5, "Average_Marks")
        print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))

        # Step 6: Identify students who may benefit from academic support.
        support_students = results[
            (results["Result"] == "Fail") |
            (results["Average_Marks"] < 50) |
            (results["Attendance_Percent"] < 75)
        ]
        display_heading("STUDENTS WHO MAY BENEFIT FROM ACADEMIC SUPPORT")
        if support_students.empty:
            print("No students matched the support indicators in this sample.")
        else:
            print(support_students[
                ["Student_ID", "Name", "Average_Marks", "Result", "Attendance_Percent"]
            ].to_string(index=False))

        # Step 7: Save analysis outputs as CSV files.
        OUTPUT_DIR.mkdir(exist_ok=True)
        results.to_csv(OUTPUT_DIR / "student_results.csv", index=False)
        subject_summary.to_csv(OUTPUT_DIR / "subject_summary.csv", index=False)
        print(f"\nAnalysis files saved in: {OUTPUT_DIR}")

    except FileNotFoundError:
        print("Error: students.csv was not found. Keep it in the project folder.")
    except (ValueError, KeyError) as error:
        print(f"Data error: {error}")

if __name__ == "__main__":
    main()
