x,y=map(str,input().split())
c=0
for i in range(0,len(x)):
    if((ord(x[i])-ord(x[i-1])!=ord(y[i])-ord(y[i-1]))):
        c=c+1
if(c>0):
    print("no")
else:
    print("yes")
