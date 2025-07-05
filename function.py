
def acount():
    a=input("Nter a string:")
    b=input("Enter the character you want to count:")
    c=0
    for i in a:
        if i==b:
            c=c+1
    return(c)
    
aur= acount()
print(aur)
       