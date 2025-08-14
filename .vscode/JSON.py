#Save Student Records (JSON), Reload, and Print
import json

# Sample student records
students = [
    {"name": "Alice", "age": 21, "major": "Computer Science"},
    {"name": "Bob", "age": 22, "major": "Mathematics"},
    {"name": "Charlie", "age": 20, "major": "Physics"}
]

# Save to JSON file
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
# Load from JSON file
with open("students.json", "r") as f:
    loaded_students = json.load(f)

# Print records
for student in loaded_students:
    print(student)

#CSV to JSON Converter in Python
import csv
import json

def csv_to_json(csv_file, json_file):
    data = []

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Convert students.csv to students.json
csv_to_json("students.csv", "students.json")
#After running this, you'll get a students.json file
[
    {
        "name": "Alice",
        "age": "21",
        "major": "Computer Science"
    },
    {
        "name": "Bob",
        "age": "22",
        "major": "Mathematics"
    },
    {
        "name": "Charlie",
        "age": "20",
        "major": "Physics"
    }
]
