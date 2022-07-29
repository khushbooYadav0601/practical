name=(input("Enter The Name Of The Person : "))
age=int(input("Enter The Age Of The Person : "))
gender=(input("Enter The Gender Of The Person : "))
l=[]

for i in range(3):
    l.append(name)
    l.append(age)
    l.append(gender)

for i in l:
    print(i)

# def gen():
#     i=0
#     while(i<10):
#         yield i
#         i+=1

# for i in gen():
#     print(i)

#create a generator function for even and odd numbers of given range.
# no=int(input("Enter The Value : "))
# def even(n):
#     i=0
#     while(i<=n):
#         if(i%2==0):
#             yield i
#         i+=1

#     j=0
#     while(j<=n):
#         if(j%2!=0):
#             yield j
#         j+=1
        

# for i in even(no):
#     print(i,end=" ")
# print("\n")
# for j in odd(no):
#     print(j,end=" ")

#create a generator function for even numbers of given range.
# no=int(input("Enter The Value : "))
# def even(n):
#     i=0
#     while(i<=n):
#         if(i%2==0):
#             yield i
#         i+=1

# for i in even(no):
#     print(i)

#create a generator function for odd numbers of given range.
# no=int(input("Enter the value : "))
# def odd():
#     for i in range(no):
#         if(i%2!=0):
#             yield i

# for i in odd():
#     print(i) 
    

#create a generator function for prime number of given range.
# no=int(input("Enter the Value : "))
# def prime():
#     for i in prime(2,no):
#         if(i%2==0):
#     print("no")    



# Write a program to check given number is palindrome or not
# rev=0
# no=int(input("Enter The Value : "))
# while no>0:
#     rem=no%10
#     no=no/10
#     rev=rev*10+rem
#     if no==rev:
#         print("The Number Is Palendrome")
#         break
#     else:
#         print("The Number Is Not Palindrome")
    

#write a program to genetrate fibonacci series upto n terms
# f=0
# j=1
# lno=int(input("Enter The Last Value : ")) 
# print(f,j,end=" ")
# for i in range (2,lno):
#     k=j+f
#     f=j
#     j=k
#     print(k, end=" ")
    
#write a program to dispaly sum of digits of number
# sum=0
# no=int(input("Enter The Value : "))
# while no>0:
#     rem=no%10
#     no=no//10
#     sum=sum+rem 

# print(sum)

# write a program to check given number is prime or not

# no=int(input("Enter The Value : "))
# for j in range(2,no):
#     for i in range(2,(j//2)+1):
#         if j%i==0:
#             # print("The Number Is Not Prime....")
#             break
#     else:
#         print(j)



#Write a Program to accept details of a person(name, age, qualificartion, city, state) and store it in a appropriate datatype
 
# name=[]
# age=[]
# Qualification=[]
# city=[]
# state=[]
# lno=int(input("Enter The Value : "))
# for i in range (lno):
#     name.append(input("Enter The Name Of Person : "))
#     age.append(int(input("Enter The Age Of The Person : ")))
#     Qualification.append(input("Enter The Qualification Of The Person : "))
#     city.append(input("Enter The City Of The Person : "))
#     state.append(input("Enter The State Of The Person : "))
# for i in range(lno):
#     print("name : ",name[i],"age : ",age[i],"Qualification : ",Qualification[i],"city : ",city[i],"state : ",state[i])