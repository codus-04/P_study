# 좌표평면위에 총 N개의 직사각형이 주어진다. 처음에 주어지는 직사각형은 빨간색이고, 그 다음 주어지는 직사각형은
# 파란색이다. 이와 같이 빨간색, 파란색 순으로 번갈아 주어지고, 겹치는 위치가 있다면 가장 마지막에 덮힌 색으로 
# 취급한다고 했을때, N개의 직사각형이 주어지고 난 뒤 파란색 영역의 총 넓이를 구하는 프로그램을 작성해라.

n = int(input())

OFFSET = 100
MAX_R = 200

checked = [
    [0] * MAX_R
    for _ in range(MAX_R)
]

for i in range(1,n+1):
    x1,y1,x2,y2 = map(int,input().split())

    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    color = 2 if i % 2 == 0 else 1

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] = color

area = 0
for x in range(MAX_R):
    for y in range(MAX_R):
        if checked[x][y] == 2:
            area += 1

print(area)