count=10
prison=["C"]*count
lucky=[]
print(prison)

for i in range(0,count,1):
    prison[i]="O"
print(prison)

for i in range(1,count,2):
    prison[i]="C"
print(prison)

for j in range(2,count,1):
    for i in range(j,count,j+1):
        if(prison[i]=="O"):
            prison[i]="C"
        else:
            prison[i]="O"
    print(prison)

for i in range(0,count,1):
    if(prison[i]=="O"):
        lucky.append(i+1)
print(lucky)
