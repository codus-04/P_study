# 학생 N명이 있다. 각 학생은 1번부터 N번까지 번호가 붙여져 있으며, 만약 한 학생이 k번 이상 벌칙을 받게 되면 벌금을
# 내야 한다. M번에 걸쳐 벌칙에 걸린 학생의 번호가 순서대로 주어질 때, 최초로 벌금을 내게 되는 학생은 누구인지를
# 알아내는 프로그램을 작성해라.

n,m,k = tuple(map(int,input().split()))

Penalized_person = [
    int(input())
    for _ in range(m)
]

penalty_num = [0] * (n+1)

ans = -1
for target in Penalized_person:
    penalty_num[target] += 1

    if penalty_num[target] >= k:
        ans = target
        break
print(ans)