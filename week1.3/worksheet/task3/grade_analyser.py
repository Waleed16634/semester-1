# Worksheet 1.3: Task 3

# Your code for the overall grade classification

import csv
import math


def get_classification(average_grade):
    grade_for_classification = math.ceil(average_grade)
    if average_grade >= 70:
        return "1"
    elif grade_for_classification >= 60:
        return "2:1"
    elif grade_for_classification >= 50:
        return "2:2"
    elif grade_for_classification >= 40:
        return "3"
    else:
        return "F"


# ask for filename of the student file
input_file_name = input("Please enter the filename of the student: ")

# open the file
with open(input_file_name, "r", newline="", encoding="utf-8") as student_file:
    student_data = csv.reader(student_file)
    next(student_data, None)

# read in the data, and for each student calculate their average grade and classification
    calculated_data = []
    for row in student_data:
        student_id = row[0]
        grades = [int(grade) for grade in row[1:] if grade.strip()]
        average_grade = sum(grades) / len(grades)
        classification = get_classification(average_grade)
        calculated_data.append(
            [student_id, f"{average_grade:.2f}", classification])

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}

# write this data out to a file named input_file_name + _out.csv 'student_data.csv' -> 'student_data.csv_out.csv'
output_file_name = input_file_name + "_out.csv"
with open(output_file_name, "w", newline="", encoding="utf-8") as output_file:
    output_data = csv.writer(output_file, lineterminator="\n")
    output_data.writerows(calculated_data)

# You can compare your output files with the 4 example files in example_outfiles folder
