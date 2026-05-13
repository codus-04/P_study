# 좌표평면 위에 가로 세로 길이가 8이고 넓이가 64인 색종이가 N장 주어진다. 이 N장 색종이의 각 좌측하단의 꼭지점이 
# 주어졌을 때, 모든 색종이가 붙여진 이후의 총 넓이를 구하는 프로그램을 작성해라.
# 단, 모든 색종이는 좌표평면위에 (-100,100)을 좌측하단으로 (100,100)을 우측상단으로 하는 정사각형 범위를 벗어
# 나지 않는다고 가정해도 좋다. 또한 겹치는 영역은 단 한번만 넓이에 포함시킨다.

OFFSET = 100
MAX_R = 200

n = int(input())
rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

checked = [
    [0] * MAX_R
    for _ in range(MAX_R)
]

for x , y in rects:
    x1 = x + OFFSET
    y1 = y + OFFSET
    x2 = x1 + 8
    y2 = y1 + 8

    for i in range(x1,x2):
        for j in range(MAX_R):
            if checked[i][j]:
                area += 1

print(area)