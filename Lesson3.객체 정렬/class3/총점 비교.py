# N이 주어지고, N명의 학생 수의 이름과 세 과목의 점수가 주어지면 총점이 낮은 순으로 정렬하여 출력하는 프로그램을 작성해라.
# 단, 이름과 총점이 같은 경우는 없다.

n = int(input())

name = []
score1 = []
score2 = []
score3 = []

students = []

for _ in rane(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(student_input[1])
    score2.append(student_input[2])
    score3.append(student_input[3])

class Student:
    def __init__(self,name,score1,score2,score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

for i in range(n):
    students.append(Student(name[i],score1[i],score2[i],score3[i]))

students.sort(key = lambda x : x.score1 + x.score2 + x.score3)

for student in students:
    print(student.name, student.score1, student.score2, student.score3)