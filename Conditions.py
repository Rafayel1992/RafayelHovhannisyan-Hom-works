

#1*. Write a Python program that accepts a word from the user and reverse it.
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

#2. Write a Python program to count that user inputed number is even or odd.
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

print('__________________________________________________')
#3. Write a Python program to find the inputed number from 100 to 400 (both included).
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%1==0) and (int(s[1])%1==0) and (int(s[2])%1==0):
        items.append(s)
print( ",".join(items))

#4. Write a Python program that get 2 numbers from user and retur Biggest, Median, Sum, Multiply, Divide and Subtract
print("Enter First Number: ")
num1 = int(input())
print("Enter Second Number: ")
num2 = int(input())
res = num1+num2
print("\nAddition Result = ", res)
res = num1-num2
print("Subtraction Result = ", res)
res = num1*num2
print("Multiplication Result = ", res)
res = num1/num2
print("Division Result = ", res)
#5. Write a Python program to get next day of a given date.
	#Expected Output:

#	Input a month [1-12]: 8
#	Input a day [1-31]: 23
#	The next date is [yyyy-mm-dd] 2016-8-24

year = int(input("Input a year: "))

if (year % 400 == 0):
    leapYear = True
elif (year % 100 == 0):
    leapYear = False
elif (year % 4 == 0):
    leapYear = True
else:
    leapYear = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month = 31
elif month == 2:
    if leapYear:
        month = 29
    else:
        month = 28
else:
    monthLength = 30
day = int(input("Input a day [1-31]: "))

if day < month:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))