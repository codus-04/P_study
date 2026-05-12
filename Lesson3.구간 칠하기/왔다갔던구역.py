# 위치 0에서 시작하여 N번의 명령에 걸쳐 움직인 뒤, 2번이상 지나간 영역의 크기를 출력하는 프로그램을 작성해라.
# 단, 명령은 "xL", "xR" 형태로만 주어진다. "xL"의 경우 왼쪽으로만 x만큼 이동해야 함을 "xR"의 경우
# 오른쪽으로 x만큼 이동해야 함을 뜻한다.

N = int(input())

events = []
cur = 0

for _ in range(N):
    cmd = input().split()
    x = int(cmd[:-1])
    d = cmd[-1]

    if d == "L":
        nxt = cur - x
    else:
        nxt = cur + x

    l = min(cur,nxt)
    r = max(cur,nxt)

    events.append((l,1))
    events.append((r,-1))

    cur = nxt

events.sort()

ans = 0
cnt = 0
prev = None

for pos, v in events:
    if prev is not None and cnt >= 2:
        ans += pos - prev
    
    cnt += v
    prev = pos

print(ans)

