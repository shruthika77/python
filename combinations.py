def factorial(fact):
    if fact==0:
      return 1
    f=1
    for i in range(1,fact+1):
        f=f*i
    return f
def combinations(string,r,comb_str='',k=0):
    if r==0:
        print(comb_str)
        return
    for i in range(k,len(string)):
        combinations(string,r-1,comb_str+string[i],k+1)
string=input("enter the string:")
n=len(string)
for r in range(1,len(string)+1):
    nc=factorial(n)//factorial(r)*factorial(n-r)
    print=("no of possible combinations of %d length=%d"%(r,nc))
    combinations(string,r)
        
