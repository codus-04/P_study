# 2011년 m월 d일로부터 2011년 m2월 d2일까지는 총 며칠이 있는지를 계산하는 프로그램을 작성해라.
# 2011년 윤년이 아닌 해이기 때문에 2월은 28일까지 있다.
# 단, 날짜 계산 시 시작일을 포함하여 세도록 한다.

m1, d1, m2, d2 = tuple(map(int,input().split()))

def num_of_days(m,d):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    total_days = 0

    for i in range(1,m):
        total_days += days[i]

    total_days += d

total_days = num_of_days(m2,d2) - num_of_days(m1,d1) + 1
print(total_days)