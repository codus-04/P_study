# 양의 정수를 원소로 갖는 길이가 N인 수열이 입력으로 주어졌을 때, 이 수열을 오름차순으로 정렬 했을 때, 각각 위치에
# 있던 원소가 어느 위치로 이동하는지 출력하는 프로그램을 작성해라.

class Number:
    def __init__(self,number,index):
        self.number = number
        self.index = index

n = int(input())
numbers = []
arr = list(map(int,input().split()))
numbers = [
    Number(num,i)
    for i, num in enumerate(arr)
]
answer = [
    0 for _ in range(n)
]

numbers.sort(key = lambda x : (x.number, x.index))

for i, number in enumerate(numbers):
    answer[number.index] + i + 1

for i in range(n):
    print(answer[i],end=' ')