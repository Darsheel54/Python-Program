n= int(input("Enter the no."))
S=0
for i in range (1,n):
    if n%i==0:
        S=S+i
if S==n:
    print(n,"is a perfect no.")
else:
    print(n,"is not a perfect no.")