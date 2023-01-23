ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
minAge = min(ages)
maxAge = max(ages)
ages.append(minAge)
ages.append(maxAge)
ages.sort()
length = len(ages)
medianAge = ages[ (length+1)//2] if length%2==1 else (ages[length//2]+ages[ (length//2)+1])/2
sumofAges = sum(ages)
averageofAges = sumofAges//length
rangeofAges = maxAge-minAge
print(minAge)
print(maxAge)
print(medianAge)
print(averageofAges)
print(rangeofAges)