"""
Subject Performance Analysis
Given a dictionary of marks for different subjects, loop over its values () to calculate and print the total marks and the average mark obtained
"""

marks = {
    "Math": 88,
    "Science": 76,
    "English": 91,
    "History": 65,
    "Computer": 95,
}
#  total  marks
total_subjects = len(marks)
total_marks = sum(marks.values())
print(f" total marks = {total_marks}")

# average of the marks
print(f" avg = {total_marks/total_subjects}")
