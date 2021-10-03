f1=open("marks.txt","r")

for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    print(list1[0])
