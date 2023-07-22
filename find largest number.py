def large(lst):
    a=sorted(lst,reverse=True)
    return a[0]
lst=[10,20,3,40,5,3,33]
print(large(lst))
