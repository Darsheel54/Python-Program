def lenlines(STRING):
    T=()
    b=[]
    a=STRING.split()
    l=len(a)
    for i in range(0,l):
       b.append(len(a[i]))
    T=tuple(b)
    print(T)
str=input("Enter the string")
lenlines(str)
        
