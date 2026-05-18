# 첫번째 직사각형이 먼저 놓여 있고, 두번째 직사각형이 그 다음 놓아졌을 때 그 이후애 남아있는 첫번째 직사각형의 잔해물을
# 덮기 위한 최소 직사각형의 넓이를 구하는 프로그램을 작성해라.

OFFSET = 1000
MAX_R = 2000

n = 2
rects = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i, (x1, y1, x2, y2) in enumerate(rects,start=1):
    x1,y1 = x1 + OFFSET, y1 + OFFSET
    x2,y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y] = i

min_x, max_x, min_y, max_y = MAX_R , 0 , MAX_R, 0
first_rect_exist = False

for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if checked[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x,x)
            max_x = max(max_x,x)
            min_y = min(min_y,y)
            max_y = max(max_y,y)


if not first_rect_exist:
    area = 0

else:
    area = (max_x - min_x + 1) + (max_y - min_y + 1)

print(area)