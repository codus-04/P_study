# A와 B가 동일한 시작점에서 출발한다. 1초에 1m씩 움직이며, A, B는 각각 N번, M번에 걸쳐 주어지는 방향으로
# 특정시간만큼 이동한다고 한다. A,B가 움직임을 시작한 이후에 최초로 만나게 되는 시간은 몇 초 뒤인지 구하는 프로그램을 작성해라.

MAX_T = 1000000

n,m = tuple(map(int,input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

time_a = 1
for _ in range(n):
    d,t = tuple(map(int,input()))
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1
for _ in range(m):
    d,t = tuple(int,input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b -1] + (1 if d == 'R' else -1)
        time_b += 1

ans = -1
for i in range(1,time_a):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)