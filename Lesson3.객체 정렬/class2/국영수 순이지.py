# n이 주어지고, n명의 학생수의 이름과 국어, 영어, 수학 세 과목의 점수가 주어지면 국어,영어,수학 순서대로
# 우선순위로 하여 과목점수가 높은 학생부터 출력하는 프로그램을 작성해라.

n = int(input())

name = []
korean = []
english = []
math = []
students = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(student_info[1])
    english.append(student_info[2])
    math.append(student_info[3])

class Student:
    def __init__(self, name, korean, english,math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

for i in range(n):
    students.append(Student(name[i],korean[i],english[i],math[i]))

students.sort(key = lambda x : (-x.korean,-x.english,-x.math))

for student in students:
    print(student.name,student.korean,student.english,student.math)