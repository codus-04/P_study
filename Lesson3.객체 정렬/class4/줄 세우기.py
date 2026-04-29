# N명의 학생에 대해 키, 몸무게 정보가 주어졌을 때, 다음의 규칙에 따라 정렬하려고 한다.
# 키가 더 큰 학생이 앞에 와야 한다.
# 키가 동일하다면, 몸무게가 더 큰 학생이 앞에 와야 한다.
# 키와 몸무게가 동일하다면, 번호가 작은 학생이 앞으로 와야 한다.

# 번호는 정보가 따로 주어지진 않고 입력된 순서대로 부여된다. 즉, 첫번째로 입력된 학생은 1,k번째로 입력된 학생은 k이다.
# 주어진 규칙에 따라 정렬한 이후 학생의 키,몸무게,번호를 출력하는 프로그램을 작성해라.

n = int(input())
students = []

class Student:
    def __init__(self, height, weight,idx):
        self.height = height
        self.weight = weight
        self.idx = idx

# 입력 + 객체 생성
for i in range(n):
    h,w = map(int,input().split())
    students.append(Student(h,w,i+1))

# 정렬
students.sort(key = lambda x : (-x.height, -x.weight,x.idx))

for student in students:
    print(student.height, student.weight, student.idx)