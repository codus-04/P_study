# n명의 이름, 키, 몸무게가 주어지면 키를 기준으로 오름차순으로 정렬하여 출력하는 프로그램을 작성해라.
# 단, 키가 동일한 경우에는 몸무게가 더 큰 사람이 먼저 나오도록 정렬해야한다.
# 키, 몸무게 둘 다 동일한 경우는 없다고 가정해도 좋다.

n = int(input())
name = []
height = []
weight = []

perinfor = []

for _ in ragne(n):
    n_i,h_i,w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

class Perinfor:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight


for i in range(n):
    perinfor.append(Perinfor(name[i],height[i],weight[i]))

perinfor.sort(key = lambda x : (x.height, -x.weight))

for p in perinfor:
    print(p.name, p.height, p.weight)

