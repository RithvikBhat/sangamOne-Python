count=100
prison=["C"]*count
lucky=[]

for j in range(0,count,1):
    for i in range(j,count,j+1):
        if(prison[i]=="O"):
            prison[i]="C"
        else:
            prison[i]="O"

for i in range(0,count,1):
    if(prison[i]=="O"):
        lucky.append(i+1)
print(lucky)
