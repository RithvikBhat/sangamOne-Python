f1=open("marks.txt","r")
names=[]
subjects=[]
sub1=[]
sub2=[]
sub1Toppers=[]
sub2Toppers=[]

for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    temp1=list1[3]
    list2=temp1.split(":")
    subjects.append(list2[0])
    sub1.append(list2[1])
    
#print(names)
#print(eng)
maxSub1=max(sub1)

for i in range(0,26,1):
    if(sub1[i]==maxSub1):
        sub1Toppers.append(names[i])
print(sub1Toppers,"are the toppers in",subjects[0],"with marks of",maxSub1)
