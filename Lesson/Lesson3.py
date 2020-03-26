import math
print(4**0.5) #指數

print(math.sqrt(5.8))

r = 3
print((r/2)*(r/2)*3.14)
area = r ** 2 * 3.14
print(area)
area1 = (r ** 2) * math.pi
print(area1)
score = [10, 30, 40, 90, 100, 61]
avg = sum(score)/len(score)
print(round(avg))

#True= 1, false=0

#if條件
x = 56
if x >= 60:
    print("及格")
    if x >= 90:
        print("棒")
    else:
        print("還好")
elif 55 <= x < 60:
    print("拜託教授調分")
elif 50 <= x < 55:
    print("差一點點")
else:
    print("被當")

print("Hello","world","!")
print("Hello \nworld \n!")
print("123", end ="") #不換行
print("456")

y = 42
value = f"Value of y is {y}" #加f可以指定去找出{}內的內容
print(value)
mathScores = [60, 70, 10, 20, 81, 63, 4]
# firstItem = f"first item in mathScores is {len(mathScores)}"
# print(firstItem)
for i in range(len(mathScores)):
    print(i, mathScores[i])





