data = input("enter heights of customer in inches : ")

def inchToCent(value):
    return value*2.54

heights = data.split()

new_list = []
for x in heights:
    value = int(x)
    new_list.append(inchToCent(value))
    
print("show centimeters list : ",new_list)