# 1번 칸 부터 N번째 칸까지 순서대로 총 N개의 칸이 있다. 이 중 Ai번째 칸 부터 Bi번째 칸까지 각각 블럭을 1씩 쌓으려는
# 명령이 총 k번 주어진다.(1<=i<=k)

# 명령을 다 수행한 이후 1번째 칸부터 N번째칸까지 쌓인 블럭의 수 중 최댓값을 출력하는 프로그램을 작성해라.

n , k = map(int,input().split())

blocks = [0 for _ in range(n+1)]

for _ in range(k):
    A,B = map(int,input().split())

    for i in range(A,B+1):
        blocks[i] += 1

print(max(blocks))