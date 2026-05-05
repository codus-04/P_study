# 2011년 11월 11일 11시 11분애서 시작하여 2011년 11월 A일 B시 C분까지 몇분이 걸리는지를 계산하는 프로그램을 작성해라.

a, b, c = tuple(map(int,input().split()))

diff = (a * 24 * 60 + b * 60 + c) - (11 * 24 *60 + 11 * 60 + 1)

if diff < 0:
    print(-1)

else:
    print(diff)