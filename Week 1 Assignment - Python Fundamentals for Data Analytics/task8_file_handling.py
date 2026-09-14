file = open("student.txt", "w")

file.write("Name: Aman\n")
file.write("Branch: BSc IT\n")
file.write("Subject: Python\n")

file.close()

file = open("student.txt", "r")

print("File Content:")
print(file.read())

file.close()
