import csv


def get_students_from_csv(path: str) -> list[dict[str, str]]:
    """Load students from the specified CSV file and return them as dictionaries.

    Args:
        path: Path to the CSV file.

    Returns:
        A list of dictionaries containing students.
    """
    with open(path, "r", encoding="utf-8", newline="") as f:
        database = list(csv.DictReader(f))
        return database


def add_student(database: list[dict[str, str]]) -> None:
    """Add students to the database.

    Args:
        database: List containing students.
    """
    while True:
        print("Enter the student's name: ")
        name = input()
        if not name.strip():  # stop adding students when no name was entered
            return

        try:
            print("Enter the student's grade: ")
            grade = int(input())
        except ValueError:
            print("Error: grade must be number!")
            continue

        if not 1 <= grade <= 5:
            print("Error: grade is not between 1 and 5!")
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
    """Search for a student by ID or name.

    Args:
        database: List containing students.
        student_id: Id of the student that is being searched for.
        name: Name of the student that is being searched for.

    Returns:
        A dictionary containing the student's information.

    Raises:
        TypeError: If a student_id is not an integer or name is not a string.
        ValueError: If student_id is less than 1, name is empty or contains
            only whitespace, or neither student_id nor name was specified.
    """
    if not database:
        print("database is empty!")
        return

    if student_id is not None:
        if not isinstance(student_id, int):
            raise TypeError("student_id must be an integer!")

        if student_id < 1:
            raise ValueError("student_id must be >= 1!")

        print("Search for student_id:")
        for row in database:
            if int(row["id"]) == student_id:
                print(
                    f"student_id: {row['id']} \nname: {row['name']} \ngrade: {row['grade']} \n"
                )
                return row

    elif name is not None:
        if not isinstance(name, str):
            raise TypeError("name must be a string!")

        if not name.strip():
            raise ValueError("name can not be empty!")

        print("Search for name:")
        for row in database:
            if row["name"] == name:
                print(
                    f"ID: {row['id']} \nName: {row['name']} \nGrade: {row['grade']} \n"
                )
                return row

    else:
        raise ValueError("Either student_id or name must be provided!")

    return


def change_grade(
    database: list[dict[str, str]], student_id: int, new_grade: int
) -> None:
    """Change the grade of a student.

    Args:
        database: List containing students.
        student_id: ID of the student that is being searched for.
        new_grade: The new grade.

    Raises:
        TypeError: If student_id or new_grade is not an integer.
        ValueError: If database is empty, student_id is less than 1, or new_grade
            is not between 1 and 5.
    """
    if not database:
        raise ValueError("database is empty!")

    if not isinstance(student_id, int):
        raise TypeError("student_id must be an integer!")

    if not isinstance(new_grade, int):
        raise TypeError("new_grade must be an integer!")

    if student_id < 1:
        raise ValueError("student_id must be >= 1!")

    if not 1 <= new_grade <= 5:
        raise ValueError("new_grade must be between 1 and 5!")

    for student in database:
        if int(student["id"]) == student_id:
            student["grade"] = str(new_grade)
            break


def store_students_into_csv(database: list[dict[str, str]], path: str) -> None:
    """Store the students in the specified CSV file.

    Args:
        database: List containing students.
        path: Path to the CSV file.
    """
    with open(path, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["id", "name", "grade"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for student in database:
            writer.writerow(student)
