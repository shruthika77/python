x=int(input())
y=int(input())

def swap(a,b):
 temp=0
 temp=a
 a=b
 b=temp
 return a,b
print(swap(x,y))
