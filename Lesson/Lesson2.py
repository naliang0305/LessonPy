mathScores = [60, 70, 10, 20, 81, 63, 4]
# print(mathScores[2])
# print(mathScores[1:6]) #不顯示第6個
# print(mathScores[-1]) #後面數來第一個
# print(mathScores[5:]) #從第五個到最後
# print(len(mathScores)) #list長度
# print(sum(mathScores))
# print(max(mathScores))
# print(min(mathScores))
# print(sum(mathScores)/len(mathScores))
#[]拿索引值
mathScores2 = []
mathScores2.append(60)
mathScores2.append(50)
mathScores2.append(70)
mathScores2.append(40) #加入list的尾端
mathScores2.insert(2, 30) #在想要的位子新增
print(mathScores2)

mathScores2[1] = 55 #指定index修改值
print(mathScores2)
mathScores2.pop() #把最右邊的值刪除
print(mathScores2)
mathScores2.append(70)
mathScores2.append(40)
print(mathScores2.count(40)) #查詢指定值在list中有幾個
print(mathScores2.index(40)) #查詢指定值在list中的index

print(33 in mathScores2) #尋找指定內容回傳truefasle
print(55 not in mathScores2)
mathScores2.remove(70) #指定已知內容刪除
print(mathScores2)

#del mathScores2[2] #刪除指定index的值
#del mathScores2[2:4] #刪除index2~3的值 4不包含
#print(mathScores2)
print(sorted(mathScores2)) #將list從小排到大
print(sorted(mathScores2, reverse=True)) #降冪排序
print(mathScores + mathScores2) #list相加

ls =[[1, 2, 3],[4, 5, 6]]
print(ls[0][2]) #取第一個list的第三個值


tuple1 = (1, 2, 3, 4, 5, 3, 1)
tuple2 = (3, 3, 4, 5, 6)
print(tuple1)
print(tuple2)
tuple3 = () #宣告空的，初始化
print(tuple1[3]) #取tuple1中的第三個index
print(tuple1.index(4)) #取得「4」在tuple1中的第一個索引
print(tuple1.count(3)) #取得值在裡面有幾個
#tuple1[2] = 10 #不能更改內部值
#print(tuple1 + tuple2) #相加

print(sorted(tuple1, reverse=True))

tuple4 = (88, 12)
x, y = tuple4  #值就會代入變數
print(x)
print(y)

print()

#Dictoinary key-value(鍵-值)，key是唯一
family = {
    "dad":"Homer",
    "mom":"Marga",
    "son":"Bart",
    "daughter":"Lisa",
}
print(family["dad"])
print(family.get("dad"))
#print(family["dog"]) #會出Error
print(family.get("dog")) #None
print("dog" in family) #是否有在dictionary
print(family.keys()) #顯示有什麼key
print(family.values())
print(family.items())
print(family)

for item in family:
    print(item)

familyb = {}
print(family)
familyb["cousin"] = "Max"
print(familyb)
familyb["cousin"] = "Eric"
print(familyb)
familyb.update({
    "uncle":"Martin",
    "aunt":"May",
})
print(familyb)
#刪除
del familyb["uncle"]
print(familyb)

print(familyb.pop("cousin")) #刪除並回傳刪除的值
print(familyb)

#set
fruits = {
    "apple",
    "banana",
    "guava",
}
fruits1 = {
    "strawberry",
    "apple",
    "banana"
}
print(fruits | fruits1) #聯集
print(fruits & fruits1) #交集
print(fruits - fruits1) #左邊有右邊沒有差集

fruits.add("watermelon")
fruits.remove("apple")  #不存在會Error
fruits.discard("apple") #不存在就不動作

print(fruits1)
print(sorted(fruits1, reverse=True)) #回傳list型態

fruits.clear() #刪除全部
print(fruits)

