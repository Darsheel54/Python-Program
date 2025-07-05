def countlines():
    F=open("Story.txt",'r')
    lines=F.readlines()
    print("Total no. of lines=",len(lines))
    a,b=0,0
    for i in lines:
        if i.endswith('y'):
            a+=1
        else:
            b+=1
    print("No. of lines ending wiyh 'y' are ",a)
    print("No. of lines not ending wiyh 'y' are ",b)
    F.close()
countlines()
