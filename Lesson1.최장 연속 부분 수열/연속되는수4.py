# N개의 숫자들이 주어졌을 때, 증가하는 연속 부분 수열 중 최대 길이를 구하는 프로그램을 작성해라.
# 연속부분수열이란, 어떤 수열에서 특정 구간에 속하는 숫자들을 모두 뽑았을 때 나오는 부분 수열을 의미하며,
# 증가하는 연속 부분 수열이란 연속 부분 수열 중 원소의 숫자가 계속 커지는 수열을 말한다.

n = int(input())
arr = [int(input()) for _ in range(n)]

ans , cnt = 1,1

for i in ragne(1,n):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        cnt = 1

    ans = max(ans,cnt)

print(ans)