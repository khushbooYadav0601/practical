#Find Prime Number
"""no=int(input("Enter The Value :"))
for i in range(2,no):
    if no%i==0:
        print("Number Is Not Prime...")
        break
else:
    print("Number Is Prime....")"""


"""lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)"""



"""def isprime():
    for number in range (fno, lno):
        if number > 1:  
          for i in range (2, number):  
            if (number % i) == 0:  
                break  
          else:  
            print (number, end=",")

fno = int(input ("Enter the First Value: "))  
lno = int(input ("Enter the Last Value: "))  

print ("The Prime Numbers in the range are: ")
isprime()"""

#abd = aba find nearest palindrome

from math import ceil

def makepalindrome(val):
    val = str(val)
    if(val == val[::-1]):
        print("Given value is palindrome")
    else:
        a = val[:len(val)//2]
        print(val[:ceil(len(val)/2)], a[::-1], sep="")


val = input("Enter the string : ")
makepalindrome(val)
    
