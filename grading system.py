print("Enter class score = ")
score = int(input())
if score>=90 and score<=100:
    print("Your Grade is A")
elif score>=80 and score<90:
    print("Your Grade is B")
elif score>=70 and score<80:
    print("Your Grade is C")
elif score>=60 and score<70:
    print("Your Grade is D")
elif score>=0 and score<60:
    print("Your Grade is F")
else:
    print("invalid Input")