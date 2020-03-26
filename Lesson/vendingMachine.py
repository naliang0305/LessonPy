# 販賣機

flag = True # 控制迴圈是否繼續執行
balance = 0 # 使用者餘額

drinks = [
    {'name': '可樂', 'price': 20},
    {'name': '雪碧', 'price': 20},
    {'name': '茶裏王', 'price': 25},
    {'name': '原萃', 'price': 25},
    {'name': '純粹喝', 'price': 30},
    {'name': '水', 'price': 20},
]
while flag:
    print('\n========================')
    select = eval(input('1. 儲值\n2. 購買\n3. 查詢餘額\n4. 離開\n請選擇'))

    if select == 1: # 儲值
        value = eval(input('儲值金額：'))
        balance += value
        print(f'儲值後餘額為{balance}元')
        while value < 1:
            # 若使用者輸入數字小於零，需要重新輸入
            print('====儲值金額需大於零====')
            value = eval(input('儲值金額：'))
    elif select == 2: # 購買
        # 印出品項
        print('\n請選擇商品')
        #for item in drinks:
            #print(f'{item["name"]} {item["price"]}元')  無法列出編號
        for i in range(0, len(drinks)):
            print(f'({i+1})\t{drinks[i]["name"]}\t{drinks[i]["price"]}元')

        choose = eval(input('請選擇編號:'))
        #buy_drink = drinks[choose-1] #邏輯確認 因為前面i+1了 會輸入到index+1的數值
        #print(f'{buy_drink["name"]}')

        while choose < 1 or choose > 6:
            print('====請輸入1-6之間====')
            choose = eval(input('請選擇:'))

        buy_drink = drinks[choose-1]
        if balance < buy_drink['price']:
            print('====餘額不足====')
        else:
            print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
            balance -= buy_drink['price']
            print(f'購買後餘額為{balance}元')
    elif select == 3: # 查詢餘額
        print(f'目前餘額為{balance}元')
    elif select == 4: # 離開
        print('bye')
        flag = 0
        break
    else:  # 重新輸入
        print('=====請輸入1-4之間=====')
        continue




