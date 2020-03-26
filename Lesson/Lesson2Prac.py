#chinese = [5, 14, 7]
#english = [23, 36, 28]
#math = [88, 80, 92]
#grades = [chinese,english,math]
grades = [[5, 14, 7],[23, 36, 28],[88, 80, 92]]
print(grades[1])
print(sum(grades[0])/len(grades[0]))
#print(sum(chinese)/len(chinese))
print(sum(grades[1])/len(grades[1]))
print(sum(grades[2])/len(grades[2]))
#science = [94, 90, 96]
#grades.append(science)
grades.append([94, 90, 96])
print(grades)
grades[0][1] = 20
print(grades)

print()

gradesTuple = ((5, 14 ,7), (23, 36, 28), (88, 80, 92))
print(gradesTuple[2])
print(sum(gradesTuple[0])/len(gradesTuple[0]))
print(sum(gradesTuple[1])/len(gradesTuple[1]))
print(sum(gradesTuple[2])/len(gradesTuple[2]))

print()

gradesDict = {
    "chinese":[5, 14, 7],
    "english":[23, 36, 28],
    "math":[88, 80, 92]
}
print(gradesDict["math"])
print(gradesDict.get("math"))
print(sum(gradesDict["chinese"])/len(gradesDict["chinese"]))
print(sum(gradesDict["english"])/len(gradesDict["english"]))
print(sum(gradesDict["math"])/len(gradesDict["math"]))

gradesDict.update({
    "science":[94, 90, 96]
})
print(gradesDict)

print()

allstudents = {
    "John","Eva","Jill","Eric","Andy","Albert","Polina","Kristin","Angela"
}
danceClub = {
    "John","Eva","Jill","Eric","Andy"
}
guitarClub = {
    "Andy","Eric","Albert","Polina","Kristin"
}
print(danceClub & guitarClub)
print(danceClub - guitarClub )
both = guitarClub | danceClub
print(allstudents - both)
print(allstudents - (danceClub | guitarClub))