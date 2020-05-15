list = [2,7,5,64,14]
count_odd = 0
count_even = 0
for x in list:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Even=",count_even,",Odd=",count_odd)
