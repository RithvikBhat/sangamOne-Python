f1=open("in1.txt","r")
f2=open("out1.txt","w")
min=int(f1.readline())
max=int(f1.readline())
info2="------------"
for num in range(min,max+1):
    for i in range(1,11):
        info1=str(num)+"*"+str(i)+"="+str(num*i)
        print(info1)
        f2.write(info1)
        f2.write("\n")
    print(info2)
    f2.write(info2)
    f2.write("\n")
f2.close()
    
    
