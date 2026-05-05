# 2011년 m1월 d1일이 월요일 이었다면, 2011년 m2월 ,d2일은 어떤 요일인지를 구하는 프로그램을 작성해라.
# 2011년은 윤년이 아닌 해이기 때문에 2월은 28일까지 있다.

m1 , d1, m2, d2 = map(int,input().split())

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def days_from_start(month, day):
    return sum(days_in_month[:month - 1]) + day

start_day = days_from_start(m1,d1)
end_day = days_from_start(m2,d2)

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

diff = end_day - start_day

result = week[diff % 7]

print(result)