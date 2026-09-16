def hello_python_exercise(num_students: int, student_name: str = "Adnan Memic") -> None:
    if not isinstance(num_students, int):
        raise TypeError("num_students must be an integer.")
    if num_students < 0:
        raise ValueError("num_students cannot be negative.")

    if not isinstance(student_name, str):
        raise TypeError("student_name must be a string.")
    if not student_name.strip():
        raise ValueError("student_name cannot be empty.")

    print(f"This course has {num_students} and one of those is {student_name}.")
