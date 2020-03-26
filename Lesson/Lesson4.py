weight = 100
weight1 = 80

def add_weight(w1, w2=1): #第二個參數被預設成1
    result = w1 + w2
    return result

x = add_weight(weight)
y = add_weight(weight, weight1)
print(x,y)

def calculate(x, y):
    return x+y, x-y, x*y, x/y

num1 = 2
num2 = 5
result = calculate(num1, num2)
print(result) #(7, -3, 10, 0.4)

r1, r2, r3, r4 = calculate(num1, num2)
print(r1, r2, r3, r4)

r1, r2, r3, r4 = calculate(y=num1, x=num2)#按照關鍵字傳入參數，順序不重要
print(r1, r2, r3, r4)


def add(x, y):
    """
    數字相加
    :param x: 數字1
    :param y: 數字2
    :return: 相加結果
    """
    return x + y