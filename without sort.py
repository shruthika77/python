list=[1,2,8,6,5]
sorted=[]
for i in range(len(list)):
    small=min(list)
    sorted.append(small)
    list.remove(small)
print(sorted)
     
        
