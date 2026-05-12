# 일직선으로 무한히 나열된 회색 타일이 있다. 이 타일은 신기한 타일이기 때문에, 현재 타일을 색이 어떤 색인지와는
# 상관없이 왼쪽으로 뒤집으면 흰색으로 바뀌고, 오른쪽으로 뒤집으면 검은색으로 바뀌게 된다.

# 아무 타일에서 시작하여 N번의 명령에 걸쳐 움직인다. 명령은 xL, xR 형태로만 주어지며, xL의 경우 왼쪽으로 이동하여
# 순서대로 현재 위치 타일 포함 총 x칸의 타일을 오른쪽으로 뒤집는다. xR의 경우 오른쪽으로 이동하며 순서대로
# 현재위치 타일 포함 총 x칸의 타일을 오른쪽으로 뒤집는다. 각 명령 이후에는 마지막으로 뒤집은 타일 위치에 서 있다고
# 가정한다. 모든 명령을 실행한 뒤의 흰색, 검은색 타일 수를 각각 출력하는 프로그램을 작성해라.

n = int(input())

segments = []
cur = 0
for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        nxt = cur - x + 1
        l , r = nxt, cur
        color = 'W'
        cur = nxt
    else:
        nxt = cur + x - 1
        l,r = cur, nxt
        color = 'B'
        cur = nxt
    
    segments.append((l, r+ 1, color))

coords = set()
for l ,r, _ in segments:
    coords.add(l)
    coords.add(r)

coords = sorted(coords)
idx = {x : i for i, x in enurment(coords)}

size = len(coords) - 1
last_color = [None] * size

for l,r,c in segments:
    for i in range(idx[l],idx[r]):
        last_color[i] = c

white = black = 0

for i in range(size):
    length = coords[i+1] - coords[i]
    if last_color[i] == 'W':
        white += length
    elif last_color[i] == 'B':
        black += length

print(white,black)