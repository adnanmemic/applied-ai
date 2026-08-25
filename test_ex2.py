from aaip import ex2

try:
    studentslist = ex2.get_students_from_csv("aaip/data/students_list.csv")
    print(studentslist)
except OSError:
    print("Error: Could not open the file!")

ex2.add_student(studentslist)
print(studentslist)

ex2.search_student(studentslist, student_id=2)
ex2.search_student(studentslist, name="someone")
ex2.search_student(studentslist, name="anybody")

ex2.change_grade(studentslist, 2, 3)
print(studentslist)

try:
    ex2.store_students_into_csv(studentslist, "aaip/data/students_list.csv")
except OSError:
    print("Error: Could not open the file!")
