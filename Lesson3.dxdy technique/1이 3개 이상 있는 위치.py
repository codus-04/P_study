# 숫자 0과 1로만 이루어진 NxN 크기의 격자 상태가 주어진다. 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는
# 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램을 작성해라. 단, 인접한 곳이 격자를 벗어나는 경우에는 숫자 1이 적혀
# 있지 않은 것으로 생각한다.

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y <n

def adjacent_cnt(x,y):
    cnt = 0
    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy
        if in_range(nx,ny) and arr[nx][ny] == 1:
            cnt += 1
    
    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i,j) >= 3:
            ans += 1

print(ans)