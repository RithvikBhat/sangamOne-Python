f1=open("marks.txt","r")
names=[]
subjects=[]
sub1=[]
sub2=[]
sub3=[]
sub4=[]
sub5=[]
tot=[]
sub1Toppers=[]
sub2Toppers=[]
sub3Toppers=[]
sub4Toppers=[]
sub5Toppers=[]
goldMedalist=[]
for i in range(0,26,1):
    
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])

    #English
    list2=list1[3].split(":")
    subjects.append(list2[0])
    sub1.append(int(list2[1]))

    #Maths
    list2=list1[4].split(":")
    subjects.append(list2[0])
    sub2.append(int(list2[1]))

    #Physics
    list2=list1[5].split(":")
    subjects.append(list2[0])
    sub3.append(int(list2[1]))

    #Chemistry
    list2=list1[6].split(":")
    subjects.append(list2[0])
    sub4.append(int(list2[1]))

    #Biology
    list2=list1[7].split(":")
    subjects.append(list2[0])
    sub5.append(int(list2[1]))

    #Total
    tot.append(sub1[i]+sub2[i]+sub3[i]+sub4[i]+sub5[i])
#print(names)
#print(eng)
maxSub1=max(sub1)
maxSub2=max(sub2)
maxSub3=max(sub3)
maxSub4=max(sub4)
maxSub5=max(sub5)
maxTot=max(tot)
                
for i in range(0,26,1):
    if(sub1[i]==maxSub1):
        sub1Toppers.append(names[i])
    if(sub2[i]==maxSub2):
        sub2Toppers.append(names[i])
    if(sub3[i]==maxSub3):
        sub3Toppers.append(names[i])
    if(sub4[i]==maxSub4):
        sub4Toppers.append(names[i])
    if(sub5[i]==maxSub5):
        sub5Toppers.append(names[i])
    if(tot[i]==maxTot):
        goldMedalist.append(names[i])
print(sub1Toppers,"are the toppers in",subjects[0],"with marks of",maxSub1)
print(sub2Toppers,"are the toppers in",subjects[1],"with marks of",maxSub2)
print(sub3Toppers,"are the toppers in",subjects[2],"with marks of",maxSub3)
print(sub4Toppers,"are the toppers in",subjects[3],"with marks of",maxSub4)
print(sub5Toppers,"are the toppers in",subjects[4],"with marks of",maxSub5)
print(goldMedalist,"are the gold medalist with marks",maxTot)
