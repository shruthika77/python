try:
    inte=int(input("enter a number"))
    print(inte)
except ValueError:
    print("inte is not a integer")
    
else:
    print("execption handling done")
finally:
    print("exception is done")
