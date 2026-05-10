# 1차원 직선 상에 N개의 선분이 놓여있다. 가장 많이 겹치는 구간에서는, 몇 개의 선분이 겹치는지를
# 구하는 프로그램을 작성해라. 단, 겹치는 구간을 찾는 문제이므로 끝점에서 닿는 경우는 겹치는 것으로 생각하지 않는다.

def max_overlap(segments):
    events = []

    for l, r in segments:
        events.append((l,1))
        events.append((r,-1))

    events.sort(key = lambda x : (x[0],x[1]))

    current = 0
    max_count = 0

    for _, value in events:
        current += value
        max_count = max(max_count,current)

    return max_count

N = int(input())
segments = [tuple(map(int,input().split())) for _ in range(N)]

print(max_overlap(segments))