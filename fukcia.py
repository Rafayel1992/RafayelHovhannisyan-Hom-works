#1. Write a function to multiply all the numbers in a given list

def multipLication(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


myList1 = [4, 5, 6]
print(multipLication(myList1))
print('_______________________________________')

#2. Write a function that takes a list and returns a new list with unique elements of the first list

def unic_elements(laist):
    return set(list)

list = [1,1,1 ,2,2,2,3,3,3]
unic_elements(list)
myUnicList = unic_elements(list)
print(myUnicList)
print('________________________________________')


#3. Write a function to print the even numbers from a given list.
def even(list1):
    enum = []
    for x in list1:
        if x % 2 == 0:
            enum.append(x)
    return enum


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even(list1)
print(even(list1))
print('____________________________________________')
#4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
    #  Sample String : 'The quick Brow Fox'
     # Expected Output :
     # No. of Upper case characters : 3
    #  No. of Lower case Characters : 12
def string_test(s):
    f = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            f["UPPER_CASE"] += 1
        elif c.islower():
            f["LOWER_CASE"] += 1
        else:
            pass

    print("No. of Upper case characters : ", f["UPPER_CASE"])
    print("No. of Lower case Characters : ", f["LOWER_CASE"])


string_test('The quick Brown Fox')
print("____________________________________________________")

#5. Write a Python function that takes a number as a parameter and check the number is prime or not
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2, n):
            if(n % x==0):
                return False
        return True
print(test_prime(99))
print('_____________________________________________________________')