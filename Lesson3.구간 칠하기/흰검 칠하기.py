# 일직선으로 무한히 나열된 타일이 있다. 아무 타일에서 시작하여 N번의 명령에 걸쳐 움직인다.
# 명령은 xL, xR 형태로만 주어지며, xL의 경우 왼쪽으로 이동하면서 현재 위치 타일 포함 총 x칸의 타일을
# 검은색으로 연속하게 칠함을 뜻한다.

# 각 명령 이후에는 마지막으로 칠한 타일 위치에 서 있다고 가정한다. 타일의 색은 덧칠해지면 마지막으로 칠해진 색으로 
# 바뀌는데, 만약 타일 하나가 순서 상관없이 흰색과 검은색으로 각각 두 번 이상 칠해지면 회색으로 바뀌고 더이상
# 바뀌지 않는다. 모든 명령을 실행한 뒤의 흰색, 검은색, 회색의 타일 수를 각각 출력하는 프로그램을 작성해라.

n = int(input)

segments = []
cur = 0
for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        nxt = cur - x + 1
        l, r = nxt, cur
        color = "W"
        cur = nxt

    else:
        nxt = cur + x -1
        l , r = cur,nxt
        color = "B"
        cur = nxt

    segments.append((l,r+1,color))


coords = set()
for l, r, _ in segments:
    coords.add(l)
    coords.add(r)

coords = sorted(coords)
idx = { x : i for i, x in enurement(coords)}

size = len(coords) - 1
white = [0] * size
black = [0] * size
last = [None] * size

for l,r,c in segments:
    for i in range(idx[l],idx[r]):
        if c == "W":
            white[i] += 1

        else:
            black[i] += 1
        last[i] = c

W = B = G = 0

for i in range(size):
    length = coords[i+1] - coords[i]
    if white[i] >= 2 and black[i] >= 2:
        G += length
    elif last[i] == 'W':
        W += length
    elif last[i] == 'B':
        B += length
print(W,B,G)