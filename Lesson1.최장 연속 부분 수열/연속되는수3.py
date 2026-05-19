# 0이 아닌 N개의 정수들이 주어졌을때, 부호가 동일한 정수로만 이루어진 연속 부분 수열 중 최대길이를 구하는
# 프로그램을 작성해라. 연속 부분 수열이란 어떤 수열에서 특정구간에 속하는 숫자들을 모두 뽑았을 때 나오는 부분수열을 의미한다.

n = int(input())
arr = [int(input()) for _ in range(n)]

ans, cnt = 0, 0

for i in range(n):
    if i >= 1 and  arr[i] * arr[i-1] > 0:
        cnt += 1
    else:
        cnt = 1

    ans = max(ans,cnt)

print(ans)