def tower_of_hanoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk from 1rod",source,"to another rod",destination)
        return
    tower_of_hanoi(n-1,source,auxiliary,destination)
    print("move disk",n,"from rod",source,"to rod",destination)
    print(n-1,auxiliary,destination,source)
n=5
tower_of_hanoi(n,'A','B','C')
        
