import csv


def get_students_from_csv(path: str) -> list[dict[str, str]] | None:
    with open(path, "r", encoding="utf-8", newline="") as f:
        database = list(csv.DictReader(f))
        return database


def add_student(database: list[dict[str, str]]) -> None:
    while True:
        print("Enter the students name: ")
        name = input()
        if not name.strip():  # stop adding students when no name was entered
            return

        try:
            print("Enter the students grade: ")
            grade = int(input())
        except ValueError:
            print("Error: Not a number!")
            continue

        if not 1 <= grade <= 5:
            print("Error: Grade is not between 1 and 5!")
            continue

        if not database:
            new_id = 1
        else:
            id_list = [int(row["id"]) for row in database]
            new_id = max(id_list) + 1

        database.append({"id": str(new_id), "name": name, "grade": str(grade)})


def search_student(
    database: list[dict[str, str]],
    student_id: int | None = None,
    name: str | None = None,
) -> dict[str, str] | None:

    if not database:
        raise ValueError("Database is empty!")

    if student_id is not None:
        if not isinstance(student_id, int):
            raise TypeError("ID must be an integer!")

        if student_id < 1:
            raise ValueError("ID must be >= 1!")

        print("Search for ID:")
        for row in database:
            if int(row["id"]) == student_id:
                print(
                    f"ID: {row['id']} \nName: {row['name']} \nGrade: {row['grade']} \n"
                )
                return row

    elif name is not None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")

        if not name.strip():
            raise ValueError("Name can not be empty!")

        print("Search for name:")
        for row in database:
            if row["name"] == name:
                print(
                    f"ID: {row['id']} \nName: {row['name']} \nGrade: {row['grade']} \n"
                )
                return row

    else:
        raise ValueError("Either ID or Name must be provided!")

    return None


def change_grade(
    database: list[dict[str, str]], student_id: int, new_grade: int
) -> None:
    if not database:
        raise ValueError("Database is empty!")

    if not isinstance(student_id, int):
        raise TypeError("ID must be an integer!")

    if not isinstance(new_grade, int):
        raise TypeError("Grade must be an integer!")

    if student_id < 1:
        raise ValueError("ID must be >= 1!")

    if not 1 <= new_grade <= 5:
        raise ValueError("Grade must be between 1 and 5!")

    for student in database:
        if int(student["id"]) == student_id:
            student["grade"] = str(new_grade)
            break


def store_students_into_csv(database: list[dict[str, str]], path: str) -> None:
    if not database:
        raise ValueError("Database is empty!")

    with open(path, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["id", "name", "grade"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for student in database:
            writer.writerow(student)
