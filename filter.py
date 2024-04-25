students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors =  filter(is_gryffindor, students)
gryffindors2 = filter(lambda s: s["house"] == "Gryffindor", students)
for gryffindor in sorted(gryffindors2, key=lambda s: s["name"]):
    print(gryffindor)
