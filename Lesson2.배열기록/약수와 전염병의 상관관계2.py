# N명의 개발자들이 있으며, T번에 걸쳐 t초에 x개발자가 y개발자와 악수를 나눈 정황이 주어진다. 1명의 개발자가 처음에
# 이 점염병을 옮기기 기작한 것이 확실해졌고, 개발자가 이 병에 감염된 후에는 정확히 k번의 악수 동안만 전염병을 옮기게
# 되고, 그 이후로부터는 전염병에 걸려 있지만 새로 옮기지는 않게 된다. 개발자들의 악수애 대한 정보와 처음 전염병애 걸려
# 있는 개발자의 번호 p만 주어졌을 때, 모든 악수를 진행한 이후에 최종적으로 누가 전염병에 걸리게 되었는지를 알아내는
# 프로그램을 작성해라. 단, 전염된 사람들끼리 만나도 전염시킨 것으로 간수해야 한다. 예를 들어, 전염된 x개발자와 전염된
# y개발자끼리 악수를 해도 전염병을 옮기게 되는 횟수에 포함시켜야 한다. 아때, 감염된 횟수에 포함 될 뿐, 이미 전염 되었던
# 사람이 재감염이 되는 것은 아님에 유의한다.

class shake:
    def __init__(self,time,person1,person2):
        self.time = time
        self.person1 = person1
        self.person2 = person2

n,k,p,t = tuple(map(int(input().split())))
shakes = []

for _ in range(t):
    time, person1, person2 = tuple(map(int.input().split()))
    skakes.append(shake(time,person1,person2))

shake_num = [0] * (n+1)
infected = [False] * (n+1)

infected[p] = True

shakes.sort(key= lambda x : x.time)

for shake in shakes:
    target1 = shake.person1
    target2 = shake.person2

    if infected[target1]:
        shake_num[target1] += 1
    if infected[target2]:
        shake_num[target2] += 1

    if shake_num[target1] <= k and infected[target1]:
        infected[target1] = True
    if shake_num[target2] <= k and infected[target2]:
        infected[target2] = True

for i in range(1,n+1):
    if infected[i]:
        print(1,end="")
    else:
        print(0,end="")