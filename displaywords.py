def displaywords():
    F=open("Story.txt",'r')
    lines=F.readlines()
    a=[]
    for i in lines:
        a=i.split()
        for j in a:
            if len(j)>3:
                print(j,end=" ")
        print()
    F.close()
displaywords()
