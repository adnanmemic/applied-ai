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

def search_student(database, student_id=None, name=None):
    if student_id is not None:
        print("Search for ID:")
        for row in database:
            if int(row['id']) == int(student_id):
                print(f"ID: {row['id']} \nName: {row['name']} \nGrade: {row['grade']} \n")
                return

    elif name is not None:
        print("Search for name:")
        for row in database:
            if row['name'] == name:
                print(f"ID: {row['id']} \nName: {row['name']} \nGrade: {row['grade']} \n")
                return