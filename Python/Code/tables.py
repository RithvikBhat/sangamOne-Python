min=int(input("Enter starting number"))
max=int(input("Enter last number"))
for num in range(min,max+1):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
    print("----------------------")
