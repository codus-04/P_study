# 정수 N이 주어지고, 바꿀 진수 B가 주어지면, 10진수인 정수 N을 B진수롤 변경하여 출력하는 프로그램을 작성해라.
# 단, B로 주어지는 진수는 4,8로 2가지가 있다.

n , b = map(int,input().split())

result = " "

if n == 0:
    result = "0"

else:
    while n > 0:
        result = str(n%b) + result
        n //= b
print(result)