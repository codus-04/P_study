# N x M 크기의 직사각형에 수 1부터 순서대로 증가 시키며 달팽이 모양으로 채우는 코드를 작성해라.
# 달팽이 모양이란 왼쪽 위 모서리에서 시작해서, 오른쪽, 아래쪽, 왼쪽, 위쪽 순서대로 더이상 채울 곳이 없을 때까지 회전하는
# 모양을 의미한다.
# N: 행(row), M: 열(column)을 의미한다.

n,m = map(int,input().split())
arr = [[0] * m for _ in range(n)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs,dys = [0,1,0,-1], [1,0,-1,0]
x,y = 0,0
dir_num = 0

arr[x][y] = 1

for i in range(2, n*m + 1):
    nx,ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx,ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x,y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print() 