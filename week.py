"""no=int(input("Enter any No: "))
if no==1:
    print("Monday")
elif no==2:
    print("Tuesday")
elif no==3:
    print("Wednwsday")
elif no==4:
    print("Thursday")
elif no==5:
    print("Friday")
elif no==6:
    print("Saturday")
elif no==7:
    print("Sunday")
else:
    print("Default")"""

#Implement python switch case statement using dictionary
def Monday():
    return "Monday"
def Tuesday():
    return "Tuesday"
def Wednesday():
    return "Wednesday"
def Thursday():
    return "Thursday"
def Friday():
    return "Friday"
def Saturday():
    return "Saturday"
def Sunday():
    return "sunday"
def Default():
    return "Default"
switcher={
    1:Monday,
    2:Tuesday,
    3:Wednesday,
    4:Thursday,
    5:Friday,
    6:Saturday,
    7:Sunday
    }
def switch(dayofweek):
    return switcher.get(dayofweek.default)()

print(switch(3))
print(switch(5))
