# 2차 평면 위에 n개의 점이 주어졌을 때, 원점에서 가까운 점부터 순서대로 번호를 출력하는 프로그램을 작성해라.
# 거리가 같은 점이 여려개인 경우, 번호가 작은 점부터 출력한다.

# 단, 여기서 거리란 멘하텆 거리를 의미한다. 두 점 (x1,y1), (x2,y2) 사이의 멘하턴 거리는 |x2-x1| + |y2-y1|로 정의된다.

n = int(input())

points=[]

for i in range(n):
    x,y = map(int, input().split())
    dist = abs(x) + abs(y)
    points.append((dist,i+1))

points.sort(key = lambda x : (x[0],x[1]))

for _, idx in points:
    print(idx)