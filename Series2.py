import math
x=int(input("Enter value of x"))
n=int(input("Enter value of n"))
S=0
for i in range (1,n+1):
    S=S+(float)(math.pow(x,i))/i
print("Sum=",S)