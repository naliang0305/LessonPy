import math
import random
mathScores = [60, 70, 10, 20, 81, 63, 4]
for score in mathScores:
    print(math.sqrt(score)*10)
print()
[print(math.sqrt(item)*10) for item in mathScores]
print()
[print(i,end="") for i in range(10)]
print()
x=1
y=0
for x in range(1, 10):
    print()
    for y in range(1, 10):
        print(x,"*",y,"=",x * y,end=" ")

print()
count = 0
while count <5:
    print("你好",end=" ")
    count +=1
else:
    print("我說完啦")

#3.輸入一個數值，輸出從1到這個數的所有奇數
# x = eval(input("輸入一個數值："))
# for i in range(1, x+1):
#     if i %2 == 1:
#         print(i)
print()

# ls = []
# rows = eval(input("rows:"))
# columns = eval(input("column:"))
# for i in range(rows):
#     ls.append([])
#     for j in range(columns):
#         num = random.randint(1, 100)
#         ls[i].append(num)

# for x in range(rows):
#     for y in range(columns):
#         print(f"{ls[x][y]}", end=" ")
#     print()
#
# for row in ls:
#     for value in row:
#         print(f"{value}", end=" ")
#     print()
#
# total = 0
# for i in range(rows):
#     for rows in ls:
#         total += sum(rows)
#     print(total)


ls = []
for i in range(3):
    ls.append([])
    for j in range(3):
        num = random.randint(1, 100)
        ls[i].append(num)

ls = []
for i in range(3):
    ls.append([])
    for j in range(3):
        num = random.randint(1, 100)
        ls[i].append(num)

ls2 = []
for m in range(3):
    ls2.append([])
    for n in range(3):
        num = random.randint(1, 100)
        ls[m].append(num)

ls3 = ls+ls2
for row in ls3:
    for value in row:
        print(f"{value}", end=" ")
    print()