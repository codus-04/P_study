# (0,0)에서 시작하여 총 N번 움직이려고 한다. N번에 걸쳐 움직이는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는
# 프로그램을 작성해라. 단 dx,dy 테크닉을 활용하여 문제를 해결해라.

n = int(input())
x,y = 0,0

dx = [1,-1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    c_dir, dist = tuple(input().split())
    dist = int(dist)

    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x,y)