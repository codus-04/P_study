#좌표평면 위 (0,0)에서 북쪽을 향한 상태에서 움직이는 것을 시작하려고 한다. N개의 명령에따라 총 N번 움직이며,
# 명령 L이 주어지면 왼쪽으로 90도 방향회전을, 명령 R이 주어지면 오른쪽으로 90도 방향전환을 하고, 명령
# F가 주어지면 바라보고 있는 방향으로 한 칸 이동하력고 한다. 이동 이후 최종위치를 출력하는 프로그램을 작성해라.

dirs = input()
x,y = 0,0
curr_dir = 3

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for c_dir in dirs:
    if c_dir == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4

    elif c_dir == 'R':
        curr_dir = (curr_dir + 1) % 4
    
    else:
        x,y = x + dx[curr_dir], y + dy[curr_dir]

print(x,y)