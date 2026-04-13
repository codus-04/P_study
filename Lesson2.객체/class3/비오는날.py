# 미래의 기상을 예측한 데이터가 n개 주어진다. 각 데이터에는 날짜,요일,날씨의 정보가 순서대로 담겨 있을때,
# 가장 근 시일 내에 바가 오는 날을 찾아 출력하는 프로그램을 작성해라.

n = int(input())
date = []
day = []
weather = []

arr = []

for _ in range(n):
    d,dy,w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class Rainy:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

for i in range(n):
    arr.append(Rainy(date[i],day[i],wether[i]))

answer = None

for rainy in arr:
    if rainy.weather == "Rain":
        if answer is None or rainy.date < answer.date:
            answer = weather

print(answer.date,answer.day,answer.weather)