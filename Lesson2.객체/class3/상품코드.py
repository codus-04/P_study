# "상품명", "상품코드" 를 같이 저장할 수 있는 class를 정의하고, 2개의 객체를 선언한 후, 하내의 객체는 
# "상품명"에 codetree, "상품코드"에 50으로 각각 초기화하고 다른 객체는 새롭게 입력 받은 값을 넣어 입출력 예제와 같이
# 출력하는 프로그램을 작성해라.

product_name,product_code = input().split()
product_code = int(product_code)

class Product:
    def __init__(self,product_name,product_code):
        self.product_name = product_name
        self.product_code = product_code

product1 = Product("codetree", 50)
product2 = Product(product_name,product_code)

s = [product1,product2]

for i in range(2):
    print(f"product {s[i].product_code} is {s[i].product_name}")