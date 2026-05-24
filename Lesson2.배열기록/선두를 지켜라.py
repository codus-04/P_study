# A와 B가 동일한 시작점에서 같은 방향으로 출발한다. 도중에 방향을 바꾸는 경우는 없고, A,B는 각각 세번 N번,M번에
# 걸쳐 주어지는 특정속도로 특정시간만큼 이동한다고 한다. 선두가 몇 번 바뀌는지 찾아 출력하는 프로그램을 작성해라.
# 단, 두 사람이 공동으로 선두를 지키는 경우, 어느 한쪽이 앞서가기 전까지는 선두가 바뀌지 않았다고 판단한다.

MAX_T = 100000

n,m = tuple(map(int,input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

time_a = 1
for _ in range(n):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a-1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b-1] + v
        time_b += 1

leader, ans = 0, 0
for i in range(1,time_a):
    if pos_a[i] > pos_b[i]:
        if leader == 2:
            ans += 1

        leader = 1
    elif pos_a[i] < pos_b[i]:
        if leader == 1:
            ans += 1

        leader = 2

print(ans)