class BreadShop:
    def __init__(self):
        self.stock = {"팥붕어빵": 10, "슈크림붕어빵" : 8, "초코붕어빵" : 5}
        self.sales = {"팥붕어빵": 0, "슈크림붕어빵" : 0, "초코붕어빵" : 0}
        self.price = {"팥붕어빵" : 1000,"슈크림붕어빵" : 1200, "초코붕어빵" : 1500}

    def order_bread(self):   #breadshop.order_bread()
        while True:    
            bread_type = input("주문할 붕어빵을 선택하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가길 원하시면 뒤로가기를 입력해주세요: ")
            if bread_type == "뒤로가기":
                break
            if bread_type in self.stock:
                bread_count = int(input("주문할 개수를 입력하세요: ")) #8
                if  self.stock[bread_type] >= bread_count:
                    self.stock[bread_type] -= bread_count
                    self.sales[bread_type] += bread_count
                    print(f"{bread_type} {bread_count}개가 판매되었습니다.")
                else:
                    print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문 가능합니다.")
            else:
                print("정신을 똑바로 차리시고 주문을 다시해주세요👺")

    def admin_mode(self):
        while True:
            bread_type = input("추가할 붕어빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '종료' 입력: ")
            if bread_type == "종료":
                break
            if bread_type in self.stock:
                bread_count = int(input("추가할 개수를 입력하세요: "))
                self.stock[bread_type] += bread_count
                print(f"{bread_type}의 재고가 {bread_count}개 추가되어 현재 {stock[bread_type]}개 입니다.")
            else:
                print("올바른 메뉴를 입력하세요.")

    def calculate_sales(self):
        # total_sales = sum(sales[key] * price[key] for key in sales)
        total = 0
        for key in self.sales:
            # total = total + (sales[key] * price[key])
            total +=(self.sales[key] * self.price[key])
        print(f"오늘의 총 매출은 {total}원 입니다.")