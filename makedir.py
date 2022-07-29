import re
ex="[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]{2,3}"
f=open("emails.txt",'r')

text=f.read()
a=re.findall(ex, text)
with open("output.txt","w") as file:
    for i in a:
        file.write(i+"\n")

f.close()