# N개의 숫자들이 주어졌을때, 연속하여 동일한 숫자가 나오는 횟수 중 최대를 구하는 프로그램을 작성해라.

n = int(input())
arr = [int(input()) for _ in range(n)]

ans, cnt = 0, 0
for i in range(n):
    if i >= 1 and arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt = 1

    ans = max(ans,cnt)

print(ans)