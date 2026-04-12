# 필요한 "해체 코드", 끊어야하는 "선의 색", "특정 초"가 주어지면 입출력 예제와 같이 출력하는 프로그램을 작성해라.
# class를 이용하여 문제를 해결해라.

unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class Bomb:
    def __init__(self,unlock_code,wire_color,seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

print(f"code : {unlock_code}")
print(f"color : {wire_color}")
print(f"second : {seconds}")