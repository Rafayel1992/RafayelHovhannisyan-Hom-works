
#1. Write a program to print odd index elements in a list
myNubers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myNubers)
print(myNubers[1])
print(myNubers[3])
print(myNubers[5])
print(myNubers[7])
print(myNubers[9])
print('_______________________________________________')
#2. Write a program to get the largest number from a list
myList = [10, 20, 4, 45, 99]
myList.sort()
print(myList[-1])
print('_________________________________________________')

#3. Write a program to remove duplicates from a list
myList1 = [12, 12, 13, 15, 16, 17, 17, 18]
print(myList1)
myList1.pop(1)
myList1.pop(5)
print(myList1)
print('___________________________________________________')
#4. Write a program to convert a string to a list
myList2 = ['naem'',''lastNaem', 'day', 'word']
myNubers1 = [1,2,5,6,7]
myList2.extend(myNubers1)
print(myList2)
print('______________________________________________________')

#5. Write a program to find the item with maximum occurrences in a given list
myList3 = [12, 12, 12, 13, 15, 16, 17, 17, 18]
myList3.count(12)
myList3.count(13)
myList3.count(15)
myList3.count(16)
myList3.count(17)
myList3.count(18)
print(myList3.count(12), myList3.count(13), myList3.count(15),myList3.count(16), myList3.count(17), myList3.count(18))
print('__________________________________________________________')
#6. Write a program to check whether a specified list is sorted or not
mylist4 = ['naem  ',' lastNaem', 'day', 'word']
mylist4.sort()
print(mylist4)
print('_____________________________________________________________')
# Heppy,yaer,and,new, Christmas,Merry
varList =['Heppy','year','and','new', 'Christmas','Merry']
varList[3], varList[2] = varList[2], varList[3]
varList[1], varList[2] = varList[2], varList[1]
varList[4], varList[5] = varList[5], varList[4]
#2 ․ Օption
varList1 =['Heppy','year','and','new', 'Christmas','Merry']
varList1[1] = 'new'
varList1[2] = 'year'
varList1[3] = 'and'
varList1[4] = 'Merry'
varList1[5] = 'Christmas'
print(varList)
print('________________________________________________________________')
print(varList1)
print('________________________________________________________________')