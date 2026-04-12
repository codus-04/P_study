# 이름, 번지수, 지역에 대한 n명의 자료가 주어지면, 사전 순으로 이름이 가장 느린 사람의 자료를 출력하는 프로그램을 작성해라.
# 단, class를 이용하여 각 사람의 정보를 담은 객체 n개 만들어 문제를 해결해라.

n = int(input())
name = []
street_address = []
region = []
info = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class Person:
    def __init__(self,name,street_address,region):
        self.name = name
        self.street_address = street_address
        self.region = region

# person 객체 생성
for i in range(n):
    info.append(Person(name[i],street_address[i],region[i]))

# 사전 순으로 이름이 가장 느린 사람 찾기
slowest = info[0]
for person in info:
    if person.name > slowest.name:
        slowest = person

print(f"name {slowest.name}")
print(f"addr {slowest.street_address}")
print(f"city {slowest.region}")