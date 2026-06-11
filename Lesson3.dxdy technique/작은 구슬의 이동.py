# 벽으로 둘러싸인 N행 N열의 각 격자 안에 한 개의 구슬이 놓여져있다. 이 구슬은 상하좌우 중 특정 방향으로 1초에 한 칸씩
# 움직인다. 가장 왼쪽 위 격자 칸을 1행 1열, 가장 오른쪽 아래 격자 칸을 N행 N열 이라고 하면 아래의 그림은 초기에
# 1행 2열에 놓여있고 왼쪽을 향하는 구슬을 나타낸 것이다.

# 구슬이 벽에 부딪히면 움직이는 방향이 반대로 뒤집혀 동일한 속도로 움직이는 것을 반복한다. 이때 방향을 바꾸는데에는
# 1만큼의 시간이 소요된다. 구슬의 처음 위치와 초기 방향이 주어졌을 때, T초가 지난 이후에 해당 구슬의 위치를 구하는
# 프로그램을 작성해라.

n , t = tuple(map(int,input().split()))
x,y,c_dir = tuple(input().split())

mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

x,y,move_dir = int(x)-1, int(y) -1, mapper[c_dir]

dxs = [0,1,-1,0]
dys = [1,0,0,-1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx,ny = x + dxs[move_dir], y + dys[move_dir]

    if in_range(nx,ny):
        x,y = nx,ny
    else:
        move_dir = 3 - move_dir
print(x+1,y+1)