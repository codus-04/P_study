# 0과 1로 이루어진 이진수로 어떤 수가 주어지면 그 수를 십진수로 변환하여 출력하는 프로그램을 작성해라.

binary = input()

num = 0
 
for i in range(8):
    num = num * 2 + binary[i]

print(num)