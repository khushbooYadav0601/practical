import re
p = input("Enter PassWord ")
x=True
while x:
    if(len(p)<5 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[@#$%^&*]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Password Is valid "+p)
        x=False
        break
    
if x:
    print("Password is Not valid ")
    