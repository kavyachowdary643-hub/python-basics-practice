import json
student = {
    "name": "Kavya",
    "age": 20,
    "branch": "IT"
}
with open("students.json", "w") as file:
    json.dump(student, file, indent=4)
print("Student data saved successfully!")
with open("students.json", "r") as file:
    data = json.load(file)
print("\nStudent Details:")
print("Name:", data["name"])
print("Age:", data["age"])
print("Branch:", data["branch"])