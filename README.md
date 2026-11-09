# Student Performance Analytics System

**Student:** Shivank Reddy  
**Roll Number:** 3PD23IS051  
**Department:** Information Science and Engineering  
**College:** PDA College of Engineering, Kalaburagi  

## Overview
A beginner-friendly Python data-analysis project that reads student marks and attendance from a CSV file and produces student-wise results, grades, pass/fail statistics, subject summaries, top performers, and academic-support indicators.

> **Dataset note:** `students.csv` contains 22 fictional/synthetic sample records for demonstration. It is not real institutional or survey data. Replace it with authorized data only when permitted.

## Technologies
- Python 3
- Pandas
- NumPy

## Project structure
```text
student_performance_analytics/
├── main.py
├── functions.py
├── students.csv
├── requirements.txt
├── README.md
├── PROJECT_DOCUMENTATION.md
└── output/                 # generated after running main.py
```

## Setup and execution
1. Install Python 3.9 or later.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```

## Dataset columns
`Student_ID`, `Name`, `Department`, four subject marks (`Python`, `Mathematics`, `Statistics`, `AI_Basics`) and `Attendance_Percent`.

## Rules used
- Each subject is marked out of 100.
- A student passes only if they score **at least 35 in every subject**.
- Grade is based on the average: A+ (90–100), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), F (below 50).
- The academic-support list flags students who failed, have an average below 50, or attendance below 75%. These are simple indicators, not a diagnosis or final academic decision.

## Output
The program prints the analysis and creates:
- `output/student_results.csv`
- `output/subject_summary.csv`

## Learning outcomes
Practice CSV handling, variables, data types, conditions, loops, reusable functions, NumPy calculations, Pandas DataFrames, filtering, sorting and basic data validation.
