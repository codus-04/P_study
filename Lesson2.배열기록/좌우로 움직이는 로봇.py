# 1차원 직선 위에서 1초에 한칸씩 좌우로만 왔다갔다 하는 로봇 A와 B가 있다. A가 움직이는 횟수 N과 B가 움직이는
# 횟수 M이 주어지고 각각 로복들이 어느 방향으로 얼만큼 움직였는지가 주어졌을 때, 로봇 A와 B가 바로 직전에는 다른
# 위치에 있다가 그 다음번에 같은 위치에 오게 되는 경우가 총 몇번인지를 구하는 프로그램을 작성해라.
# 단 로봇 A, B는 처음에 같은 지점에서 움직이며 이는 횟수에 포함시키지 않는다. 또한 각 로복이 움직임을 종료한 이후에는
# 같은 위치에 계속 머물러 있으며 이때 역시 다른 로봇이 움직임에 따라 두 로봇이 같은 위치에 오게 될 수도 있다.
# 다만, 모든 로봇이 움직인 이후의 상황은 생각하지 않는다.

MAX_T = 1000000

n,m = tuple(map(int,input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

time_a = 1
for _ in range(n):
    t,d = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a-1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1
for _ in range(m):
    t,d = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b-1] + (1 if d == 'R' else -1)
        time_b += 1

if time_a < time_b:
    for i in range(time_a,time_b):
        pos_a[i] = pos_a[i-1]
elif time_a > time_b:
    for i in range(time_b,time_a):
        pos_b[i] = pos_b[i-1]

cnt = 0

time_max = max(time_a,time_b)
for i in range(1,time_max):
    if pos_a[i] == pos_b[i] and pos_a[i-1] != pos_b[i-1]:
        cnt += 1

print(ans)