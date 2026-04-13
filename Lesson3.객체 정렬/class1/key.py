# n명의  이름, 키, 몸무게가 주어지면 키를 기준으로 오름차순으로 정렬하여 출력하는 프로그램을 작성해라
# 단, 동일한 키가 주어지지 않는다고 가정해도 좋다.

n = int(input())
name = []
height = []
weight = []
students = []

for _ in range(n):
    n_i,h_i,w_i = input().split()
    name.append(n_i)
    height.append(h_i)
    weight.append(w_i)

class Student:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

for i in range(n):
    students.append(Student(name[i],height[i],weight[i]))

students.sort(key = lambda x : x.height)

for student in students:
    print(student.name,student.height,student.weight)