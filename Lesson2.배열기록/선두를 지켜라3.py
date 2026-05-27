# A와 B가 동일한 시작점에서 같은 방향으로 출발한다. 도중에 방향을 바꾸는 경우는 없고, A, B는 각각 N번, M번에 걸쳐
# 주어지는 특정속도로 특정시간만큼 이동한다고 한다. 이 경기는 특이하게 매 시간마다 현재 선두인 사람들을 모아 명예의 전당에
# 그 이름을 올려준다. A,B의 움직임에 대한 정보가 주어졌을 때, 명예의 전당에 올라간 사람의 조합이 총 몇 번 바뀌었는지
# 출력하는 프로그램을 작성해라.

MAX_T = 1000000

n,m = map(int,input().splitI())
pos_a = [0] * (MAX_T + 1)
pos_b = [0] * (MAX_T + 1)

time_a = 1
for _ in range(n):
    v,t = map(int,input().split())
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v,t = map(int,input().split())
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b-1] + v
        time_b += 1

ans = 0

if pos_a[1] > pos_b[1]:
    prev = 1
elif pos_a[1] < pos_b[1]:
    prev = 2

else:
    prev = 0

ans = 1

for i in range(2,time_a):
    if pos_a[i] > pos_b[i]:
        curr = 1
    elif pos_a[i] < pos_b[i]:
        curr = 2
    else:
        curr = 0

    if curr != prev:
        ans += 1
        prev = curr
print(ans)