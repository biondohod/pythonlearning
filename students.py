import csv

name = input("What's ur name? ")
home = input("Where's ur home? ")

with open("students.csv") as  file:
  keys = csv.DictReader(file).fieldnames

with open("students.csv", "a", newline='') as file:
  writer = csv.DictWriter(file, fieldnames=keys)
  writer.writerow({"name": name, "home": home})