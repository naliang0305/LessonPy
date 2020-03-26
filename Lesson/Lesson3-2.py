import math
import random
#迴圈
for i in range(0, 10):
    print(i,end="")
print()
for i in range(10):
    print(i,end="")
print()
for i in range(0, 10, 2):  #(開始值,結束值,間隔)
    print(i,end="")
print()
family = {
    "dad":"Homer",
    "mom":"Marga",
    "son":"Bart",
    "daughter":"Lisa",
}

for member in family.items():
    print(member)

for key, value in family.items():
    print(f"my {key} is {value}")

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("loop end")
mathScores = [60, 70, 10, 20, 81, 63, 4]
for score in mathScores:
    if score > 80:
        break
    print(score)
for score in mathScores:
    if score > 80:
        #print("超過80")
        continue
    print(score)

    i = random.randint(1, 50)  # 1~3包含3
    print(i)

    x = eval(input('How many rows：'))#eval
    print(type(x))