from aaip import ex2

studentslist = ex2.get_students_from_csv('aaip/data/students_list.csv')
print(studentslist)

ex2.add_student(studentslist)
print(studentslist)