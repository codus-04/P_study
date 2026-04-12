# 5명의 코드네임과 점수를 입력 받아 점수가 제일 낮은 요원의 정보를 출력하는 프로그램을 작성해라.
# class를 이용하여 각 사람의 정보를 담은 객체를 5개 만들어 문제를 해결해라.

MAX_N = 5

codenames = []
scores = []
spys = []

for _ in range(MAX_N):
    codename, score = input().split()
    codename.append(codename)
    score.append(int(score))

class Spy:
    def __init__(self,codename,score):
        self.codename = codename
        self.score = score
# spy 객체 5개 생성
for i in range(MAX_N):
    spys.append(Spy(codenames[i],scores[i]))

# 점수가 제일 낮은 요원찾기
min_spy = spys[0]
for spy in spys:
    if spy.score < min_spy.score:
        min_spy = spy

print(min_spy.codename, min_spy.score)