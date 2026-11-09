# PROJECT DOCUMENTATION
## Student Performance Analytics System

### 1. Project Title and Student Details
**Project Title:** Student Performance Analytics System  
**Student Name:** Shivank Reddy  
**Roll Number:** 3PD23IS051  
**Department:** Information Science and Engineering  
**College:** PDA College of Engineering, Kalaburagi  

### 2. Objective
The objective is to develop a Python-based application that organizes student marks and attendance, calculates academic results, and presents useful summaries. It demonstrates how basic data analysis can make a dataset easier to understand.

### 3. Technologies Used
- Python 3
- NumPy for numerical calculations
- Pandas for CSV loading, DataFrame operations, filtering and sorting

### 4. Dataset Description
The included CSV contains 22 fictional sample student records. Fields include student ID, name, department, marks in Python, Mathematics, Statistics and AI Basics, and attendance percentage. The data is synthetic and must not be represented as actual college records.

### 5. Implementation
1. Read `students.csv` into a Pandas DataFrame.
2. Validate required columns and check that marks and attendance are within 0–100.
3. Use NumPy arrays to calculate each student's total and average marks.
4. Use a function and conditional statements to assign grades.
5. Identify pass/fail status. The pass condition is at least 35 marks in every subject.
6. Use a loop to calculate each subject's average, highest and lowest marks.
7. Use Pandas filtering and sorting to identify top performers and students who may benefit from academic support.
8. Save student-wise and subject-wise results as CSV files.

### 6. Key Features
- CSV dataset loading
- Input validation
- Total and average marks
- Grade assignment
- Pass/fail calculation
- Class-level statistics
- Subject-wise performance summary
- Top-five student list
- Academic-support indicator list
- Export of analysis results to CSV

### 7. Output / Screenshots
Run `python main.py` and capture screenshots of:
- Student-wise results
- Overall class summary
- Subject-wise performance
- Top-five performers
- Academic-support indicator list

Insert the actual screenshots here after running the program. Do not use fabricated screenshots.

### 8. Final Outcome
The project successfully demonstrates a basic student-performance analysis workflow using Python, NumPy and Pandas. It converts a CSV dataset into readable summaries and output files. Results depend on the dataset and the rules defined in the program.

### 9. Challenges and Learning
Possible implementation challenges include handling CSV columns consistently, validating numerical values, applying grade conditions correctly, and organizing calculations into reusable functions. The project provides practice with Python fundamentals, NumPy arrays, Pandas DataFrames, loops, conditions and data analysis.

### 10. GitHub Repository
Add the public repository URL here after creating and verifying the GitHub repository: **[Paste GitHub URL]**

---
**Important limitation:** Marks and attendance are only indicators. A low score or attendance value alone cannot explain why a student is struggling or determine what support they need. Any real-world use should follow institutional privacy rules and involve educators.
