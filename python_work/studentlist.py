import json

students_data = []
studentid1 = int(input("Enter first Student id: "))
studentname1 = input("Enter Student Name: ")
experience1 = input("Enter Student Experience: ")
skills1 = input("Enter Student Skills: ")
qualification1 = [
    {"name": input("Enter first qualification name: "), "passingyear": int(input("Enter passing year: "))},
    {"name": input("Enter second qualification name: "), "passingyear": int(input("Enter passing year: "))}
]
students_data.append({
    "studentid": studentid1,
    "studentname": studentname1,"experience": experience1,"skills": skills1,"qualification": qualification1})
studentid2 = int(input("Enter second Student id: "))
studentname2 = input("Enter Student Name: ")
experience2 = input("Enter Student Experience: ")
skills2 = input("Enter Student Skills: ")

qualification2 = [
    {"name": input("Enter qualification name: "), "passingyear": int(input("Enter passing year: "))}
]
students_data.append({
    "studentid": studentid2,
    "studentname": studentname2,"experience": experience2,"skills": skills2,"qualification": qualification2})
print("Students Data:")
print(json.dumps(students_data, indent=4))
