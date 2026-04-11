#'비밀코드', '접선장소', '시간'이 주어지면 입출력 예제 같이 출력하는 프로그램을 작성해라
# 단, class를 이용해 문제를 해결해라.

class Spy:
    def __init__(self,secret_code,meeting_point,time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time


    def printspy(self):
        print(f"secret code : {self.secret_code}")
        print(f"meeting point : {self.meeting_point}")
        print(f"time : {self.time}")