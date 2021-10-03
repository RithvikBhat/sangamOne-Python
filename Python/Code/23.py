f1=open("marks.txt","r")
names=[]
subjects=[]
eng=[]
engToppers=[]

for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    temp1=list1[3]
    list2=temp1.split(":")
    subjects.append(list2[0])
    eng.append(list2[1])
    
#print(names)
#print(eng)
maxEng=max(eng)

for i in range(0,26,1):
    if(eng[i]==maxEng):
        engToppers.append(names[i])
print(engToppers,"are the toppers in",subjects[0],"with marks of",maxEng)
