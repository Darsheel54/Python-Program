import math
x=int(input("Enter value of x"))
n=int(input("Enter value of n"))
S=0
for i in range (0,n+1):
    S=S+math.pow(x,i)
print("Sum=",S)