# 정수 A와 B가 주어지고, A진수로 표현된 어떤 수 N이 주어지면, N을 B진수로 변환하여 출력하는 프로그램을 작성해라.

a , b = map(int,input().split())
n = input()

decimal = 0
for ch in n:
    decimal = decimal * a + int(ch)

digits = []

if decimal == 0:
    digits.append(0)

else:
    while decimal > 0:
        digits.append(decimal % b)
        decimal //= b

for d in digits[::-1]:
    print(d,end=" ")