from fishbread_model import BreadShop

shop = BreadShop()

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ") #주문
    #mode = "종료"
    if mode == "종료":
        shop.calculate.sales()
        print("시스템을 종료합니다.")
        break
    elif mode == "주문":
        shop.order_bread()
    elif mode == "관리자":
        shop.admin_mode()

#로직이 숨겨지고 / 로직들만 별도 관리하니까 유지보수 쉽습니다
