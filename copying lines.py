f1=open("Story.txt",'r')
f2=open("New.txt",'w')
S=f1.readlines()
for i in S:
    if i[0]=="A" or i[0]=="a":
        f2.write(i)
print("written successfully")
f1.close()
f2.close()
