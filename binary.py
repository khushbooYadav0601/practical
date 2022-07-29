# from sqlite3 import enable_shared_cache

print("chose a no for converstion")

choice=int(input("\n 1.decimal \n 2.binary \n 3.octal \n 4.hexadecimal \n"))
conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
hexa_decimal = ''
decimal = int(input("Enter a decimal number \n"))
binary = 0
octal=0
remainder=0

ctr = 0
temp = decimal  #copy input decimal
if choice==2:
    #find binary value using while loop
    while(temp > 0):
        binary = ((temp%2)(10*ctr)) + binary
        temp = int(temp/2)
        ctr += 1

    #output the result       
    print("Binary of {x} is: {y}".format(x=decimal,y=binary))

elif choice==3:
 
    #computing octal using while loop
    while(temp > 0):
        octal += ((temp%8)(10*ctr))  #Stacking remainders
        temp = int(temp/8)             #updating dividend
        ctr += 1
        
    print("Binary of {x} is: {y}".format(x=decimal,y=octal))    

elif choice==4:
    while(decimal>0):
        remainder = decimal%16
        hexa_decimal = conversion_table[remainder]+ hexa_decimal
        decimal = decimal//16
        
    print("Hexadecimal: ",hexa_decimal)

elif choice==1:
    if decimal==decimal:
        print("no is alredy in decimal")
