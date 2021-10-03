#Prints 100 since this is an array of integers
marks1=[96,98,100]
print(max(marks1))

#prints 98 since this is an array of strings, it compares character by character,i.e,
#(9,9,1) - 9 is max
#(6,8) - 8 is max
#So 98 is max of 96,98,100

marks2=["96","98","100"]
print(max(marks2))
