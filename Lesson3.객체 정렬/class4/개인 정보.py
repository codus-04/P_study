# 5명의 이름, 키, 몸무게가 주어지면 이름순으로 정렬하여 출력하고, 키가 큰 순으로 정렬하여 출력하는 프로그램을 작성해라.
# 단, 동일한 이름과 키가 주어지지 않는다고 가정해도 좋다.

n = 5
name = []
height = []
weight = []

perinfor = []

for _ in range(n):
    n_i,h,w = input().split()
    name.append(n_i)
    height.append(int(h))
    weight.append(float(w))

class Perinfor:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

for i in range(n):
    perinfor.append(Perinfor(name[i],height[i],weight[i]))

# 이름 순 정렬(오름차순)
perinfor.sort(key = lambda x : x.name)
print("name")
for P in perinfor:
    print(p.name,p.height,p.weight)

# 키 큰 순 정렬
perinfor.sort(key = lambda x : -x.height)
print()
print("height")
for P in perinfor:
    print(p.name,p.height,p.weight)