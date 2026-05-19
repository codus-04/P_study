# N개의 수로 이루어진 수열 정보와 정수 T가 주어졌을 때, T보다 큰 수로만 이루어진 연속 부분 수열 중 최대 길이를 구하는
# 프로그램을 작성헤라. 연속 부분 수열이란, 어떤 수열에서 특정 구간에 속하는 수들을 모두 뽑았을 때 나오는 수열을 말한다.

n = int(input())
arr = [list(map(int,input().split()))for _ in range(n)]

ans = 0
cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        cnt = 0

    ans = max(ans,cnt)

print(ans)