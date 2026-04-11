# "아이디" , "레벨" 을 같이 저장할 수 있는 형태(class)를 정의하고, 2개의 객체를 선언한 후, 하나의 객체는
# "아이디"에 codetree, "레벨"에 10으로 각각 초기화하고 다른 객체는 새롭게 입력 받은 값을 넣어 입출력 예제와 같이
# 촐력하는 프로그램을 작성해라.

class User:
    def __init__(self,user_id =" ",level=0):
        self.user_id = user_id
        self.level = level

user1 = User()

user1.user_id = "codetree"
user1.level = 10

user2_id, level2 = tuple(input().split())

user2 = User()

user2.userid = user2_id
user2.level = int(level2)

print(f"user {user1.user_id} lv {user1.level}")
print(f"user {user2.user_id} lv {user2.level}")