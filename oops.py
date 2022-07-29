"""class add:
    addcount=0
    def __init__(self,fno,sno):
        self.fno=fno
        self.sno=sno
    def displayadd(self):
        print("Total : ",self.fno+self.sno)
sum=add(12,34)

sum.displayadd()"""

"""class add:
    addcount=0
    def __init__(self,fno,sno):
        self.fno=fno
        self.sno=sno
        
    def displayadd(self):
        print("Total : ",self.fno+self.sno)
        
fno=int(input("Enter The First Value : "))
sno=int(input("Enter The Second Value : "))
sum=add(fno,sno)
sum.displayadd()"""

class bmi:
    bmicount=0
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height

    def displaybmi(self):
        self.b=self.weight/(self.height**2)
        print("Your BMI Is : ",self.b)

name=input("Enter Your Name : ")
age=int(input("Enter Your Age : "))
weight=float(input("Enter Your Weight : "))
height=float(input("Enter Your Height : "))
bmi1=bmi(name,age,weight,height)
bmi1.displaybmi()
    
        
"""class bmi:
    bmicount=0
    def __init__(self,age,weight,height,name):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
       # bmicount +=1
        
    def displaycount(self):
        print("BMI = ", self.weight/self.height*self.height)
    def displaybmi(self):
        print("Name :", self.name,"Age :", self.age,"Weight :", self.weight,"Height :",self.height)

bmi=bmi("Khushi",23,33,152)
bmi=bmi(name,age,weight,height)
bmi.displaybmi()"""


""""class student:
    emp count=0
    def__init__(self,name,marks):
        self.name=name
        self.marks=marks
        students.empcount +=1
    def displaycount(self):
        print("Total Student %d" % Employe.empcount)
    def displaystudent(self):
        print()"""
    
        
