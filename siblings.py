#creating tuples brothers and sisters
sisters=("Krithika","madhu")
brothers=("abhi","rahul","krishna","venkat" , "shiva")
print("brothers are : ",brothers)
print("sisters are : ",sisters)

#joining brothers and sisters tuples to siblings
siblings=brothers+sisters
print("siblings are : ",siblings)
print("number of siblings are : ",len(siblings))

#modifying siblings tuple by adding father name and mother name
family_members=("father","mother")+siblings
print("family members are : ",family_members)