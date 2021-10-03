import datetime
today=datetime.datetime.now()
f2=open("out3.txt","a")
s1="The time now is:"
f2.write(s1+str(today))
f2.write("\n")
f2.close()
    
