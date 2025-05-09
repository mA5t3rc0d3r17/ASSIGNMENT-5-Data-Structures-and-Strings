# Dictionary containing student names as keys and their marks as values
student_dict = {"Alice": 85, "James": 90, "Jessie": 23}

# Get input from user for student name
name = input("Enter the student's name: ")

# Check if the name exists in the dictionary
if name in student_dict:
    # If found, print the student's marks
    print(str(name) + "'s marks: " + str(student_dict[name]))
else:
    # If not found, print a message
    print("Student not found.")