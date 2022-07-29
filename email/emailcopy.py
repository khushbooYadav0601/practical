import re 
f=open("email.txt","r")
text=f.readlines()
f.close()
f1=open("email2.txt","r")
text1=f1.readlines()
f1.close()
f2=open("email1.txt","w")
for s in text:
    if re.match("(.*)@(.*).(.*)", s):
        f2.write(s)
for s1 in text1:
    if re.match("(.*)@(.*).(.*)", s1):
        f2.write(s1)
f2.close()
print("File copy")
