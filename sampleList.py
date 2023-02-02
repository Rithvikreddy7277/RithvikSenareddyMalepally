sample_List=[1,2,3,3,3,3,4,5]
unique_List=[]
for i in sample_List:
    if i not in unique_List:
        unique_List.append(i)
print(sample_List)
print(unique_List)