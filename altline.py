#write a python program to display alternate lines from the file 
import re
f=open("demo.txt","r")
text=f.read()
text1=text.split("\n")
for i in range(len(text1)):
    if(i%2==0):
        print(text1(i))  
