""" Generate CSV file with name and email of students with no commits

This script allows to identify the students that have made no commits at all
by generating a file named no_commits.csv containing their name and email.

This script doesn't require any additional library.
"""
import csv
import json

students = []
students_info = {}

# Get from a csv file students information in "students_info" dictionary
# Key: handle - Value: email
with open("students_.csv") as students_data_file:
    reader = csv.reader(students_data_file)
    header = True
    for row in reader:
        if header:
            header = False
        else:
            students_info[row[1].lower()] = row[2]

# Get from a JSON file students with no commits in a "students" list.
# Each item of the list contains a dictionary with 2 entries name/handle.
with open("stats.json") as stats_file:
    data = json.load(stats_file)
    for k, v in data.items():
        if v["no_of_commits"] == 0:
            student = {"name": v["name"], "handle": k}
            students.append(student)

# Write a CSV file "no_commits.csv" with name/email.
# A matching is done from the information provided from the 2 files above.
with open("no_commits.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Email"])
    for student in students:
        writer.writerow([student["name"], students_info[student["handle"]]])
