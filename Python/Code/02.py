f1=open("in1.txt","r")
min=int(f1.readline())
max=int(f1.readline())
for num in range(min,max+1):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
    print("------------------")
