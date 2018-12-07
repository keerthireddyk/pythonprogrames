b,z=map(int,input().split())
f=[]
count=0
if(b<=2<=z):
        f.append(2)
        count=count+1
if(b<=3<=z):
        f.append(3)
        count=count+1
if(b<=5<=z):
        f.append(5)
        count=count+1
if(b<=7<=z):
        f.append(7)
        count=count+1
for x in range(b,z+1):
    if(x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0):
        f.append(x)
        count=count+1
print(count)


