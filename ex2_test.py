from aaip import ex2

studentslist = ex2.get_students_from_csv('aaip/data/students_list.csv')
print(studentslist)

ex2.add_student(studentslist)
print(studentslist)

ex2.search_student(studentslist, student_id=2)
ex2.search_student(studentslist, name="someone")

ex2.change_grade(studentslist, 2, 3)
print(studentslist)

ex2.store_students_into_csv(studentslist, 'aaip/data/students_list.csv')