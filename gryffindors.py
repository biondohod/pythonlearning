students = ["Hermione", "Harry",  "Ron"]
#list comprehension
gryffindors_list = [{"name": student, "house":"Gryffindor"} for student in students]
#dict comprehension
gryffindors_dict = {student: "Gryffindor" for student in students}

#enumerate
for i, student in enumerate(students):
    print(i + 1, student)