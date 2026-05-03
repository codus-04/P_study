# 2011년 11월 11일 A시 B분에서 시작하여 2011년 11월 11일 C시 D분까지 몇분이 걸리는지를 계산하는 프로그램을 작성해라.

A,B,C,D = map(int,input().split())

start = A * 60 + B
end = C * 60 + D

print(end-start)