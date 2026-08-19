import csv

def get_students_from_csv(path):
    try:
        with open(path, "r", encoding="utf-8", newline='') as f:
            database = list(csv.DictReader(f))
            return database
    except OSError:
        print("Error: Could not open the file!")

def add_student(database):
    while True:
        print("Enter the students name: ")
        name = input()
        if not name.strip(): # to detect even just spaces in the name
            return

        print("Enter the students grade: ")
        grade = int(input())
        if not 1 <= grade <= 5:
            return

        if not database:
            new_id = 1
        else:
            id_list = [int(row['id']) for row in database]
            new_id = max(id_list) + 1

        database.append({
            'id': new_id, 
            'name': name,
            'grade': grade
        })

def search_student(database, student_id=None, name=None):
    if not database:
        return

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

def change_grade(database, student_id, new_grade):                
    if not database:
        return
    if not isinstance(student_id, int) or student_id < 1:
        return
    if not isinstance(new_grade, int) or not 1 <= new_grade <= 5:
        return

    for student in database:
        if int(student['id']) == student_id:
            student['grade'] = new_grade
            break

def store_students_into_csv(database,path):
    if not database:
        return

    try:
        with open(path, "w", encoding="utf-8", newline='') as f:
            fieldnames = ["id", "name", "grade"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for student in database:
                writer.writerow(student)
    except OSError:
        print("Error: Could not open the file!")