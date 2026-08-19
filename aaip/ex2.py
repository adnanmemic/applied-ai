import csv

def get_students_from_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        database = list(csv.DictReader(f))
        return database

def add_student(database):
    while True:
        print("Enter the students name: ")
        name = input()

        if name == "":
            return

        print("Enter the students grade: ")
        grade = input()

        if not database:
            new_id = 1
        else:
            id_list = [int(row['id']) for row in database]
            new_id = max(id_list) + 1

        database.append({
            'id': str(new_id), 
            'name': name,
            'grade': grade
        })