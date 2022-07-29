import re
f=input("Enter File Name ")
f1=open(f,"r")
c=f1.readlines()
f2=open("email.txt","w")
for s in c:
    if re.match("(.*)@(.*).(.*)", s):
        f2.write(s)
        
no = '(?:\+[1-9]\d{0,2}[- ]?)?[1-9][0-9]{9}' 
#no='[0-9]{10}'
f3 = open('phone.txt','w+')
for line in c:
    out = re.findall(no,line)
    for i in out :
        f3.write(i + '\n')
        
        
print("Phone Number and Email Extract From File ")