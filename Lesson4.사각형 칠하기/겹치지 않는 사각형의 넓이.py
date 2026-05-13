# 좌표평면 위에 직사각형 A,B를 먼저 붙이고 그 위에 직사각형 M을 붙였다. 아직 남아 있는 (M으로 덮이지 못한)
# 직사각형 A,B의 넓이의 합을 구하는 프로그램을 작성해라. 단, 직사각형 A,B는 겹치지 않게 주어진다고 가정해도 좋다.

OFFSET = 1000
MAX_R = 2000

n = 3
rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

checked = [
    [0 * (MAX_R + 1)
     for _ in range(MAX_R+1)]
]
for i, (x1,y1,x2,y2) in enumerate(rects,start=1):
    x1,y1 = x1 + OFFSET, y1 + OFFSET
    x2,y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] = i

area = 0
for x in range(0,MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y] == 1 or checked[x][y] == 2:
            area += 1

print(area)