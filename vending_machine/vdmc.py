from vending_machine.data import Drink

balance = 0 # 使用者餘額

drinks = [
    Drink('可樂',20),
    Drink('雪碧',20),
    Drink('茶裏王',25),
    Drink('原萃',25),
    Drink('純粹喝',30),
    Drink('水',20),
]

def deposit():
    """
    儲值
    :return: nothing
    """
    global balance #宣告函式中會用到全域變數balance

    value = eval(input('儲值金額：'))
    while value < 1:
        # 若使用者輸入數字小於零，需要重新輸入
        print('====儲值金額需大於零====')
        value = eval(input('儲值金額：'))
    balance += value
    print(f'儲值後餘額為{balance}元')

def buy():
    """
    購買
    :return: nothing
    """
    global balance, drinks #宣告函式中會用到全域變數balance, drinks 要用到很多全域變數時逗號隔開即可
    #印出品項
    #print('\n請選擇商品')
    for i in range(0, len(drinks)):
        (f'({i+1})\t{drinks[i].get_name}\t{drinks[i].price}元')

    choose = eval(input('請選擇編號:'))
    # buy_drink = drinks[choose-1] #邏輯確認 因為前面i+1了 會輸入到index+1的數值
    # print(f'{buy_drink["name"]}')

    while choose < 1 or choose > 6:
        print('====請輸入1-6之間====')
        choose = eval(input('請選擇:'))

    buy_drink = drinks[choose - 1]
    while balance < buy_drink.price:
        print('====餘額不足，需要儲值嗎？====')
        want_deposit = input('y/n？')
        if want_deposit == "y":
            deposit()
        elif want_deposit == "n":
            break
        else:
            print('====請重新輸入====')

    # 儲值後餘額大於商品金額再購買
    if balance >= buy_drink.price:
        print(f'已購買{buy_drink.name} {buy_drink.price}元')
        balance -= buy_drink.price
        print(f'購買後餘額為{balance}元')

