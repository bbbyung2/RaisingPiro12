from boss import *
from student import *

f = open("st_name.txt", 'r', encoding='UTF8')
students = []

jeoung = boss('jeoung')
for i in range(28):
    st_read = f.readline()
    students.append(student(st_read.rstrip('\n')))
print(jeoung.b_name)
print(students[0].st_name)


