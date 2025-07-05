def countmy(SUBJECT):
    L=len(SUBJECT)
    for i in range(1,L+1):
        if len(SUBJECT[i])>=5:
            print((SUBJECT[i]).upper())
d={}
n=int(input("Enter the no. of subjects"))
for j in range(1,n+1):
    d[j]=input("Enter the subject")
countmy(d)
