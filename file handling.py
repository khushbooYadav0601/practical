import os
if os.path.exists("sample.txt"):
    fr=open("sample.txt","r")
    fw=open("test.txt","w")

    s=fr.read()
    print(s)
    fw.write(input("Enter the Input: "))
    
    fr.close()
    fw.close()
else:
    print("file not exists")