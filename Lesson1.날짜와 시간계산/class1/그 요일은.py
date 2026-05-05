# 2024년 m1월 d1일이 월요일 이었다면, 2024년 m2월 d2일까지 A요알은 몇 번 등장하는지 구하는 프로그램을 작성해라.
# 단, 2024년은 윤년이기 때문에 2월은 29일까지 있으며, (m1,d1)이  (m2,d1)보다 앞 선 날짜로 주어지는 경우는
# 없다고 가정해도 좋다.

m1, d1, m2, d2 = map(int,input().split())

A = input()

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def days_from_start(month,day):
    return sum(days_in_month [:month - 1]) + day

start_day = days_from_start(m1,d1)
end_day = days_from_start(m2,d2)

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

count = 0

for i in range(start_day, end_day + 1):
    weekday = week[(i - start_day) % 7]
    if weekday == A:
        count += 1

print(count)