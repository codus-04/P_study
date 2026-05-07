# 이진수로 표현되는 자연수 N이 주어지면 십진수로 바꿔 17배를 하고 다시 이진수로 나타내어 출력하는 프로그램을 작성해라.

n = int(input())

digits = []

num = 0

for i in range(len(n)):
    num = num * 2 + int(n[i]) * 17

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n%2)
    n //= 2

for digit in digits[::-1]:
    print(digit,end=" ")