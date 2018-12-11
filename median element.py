n=int(input())
b=input().split()
i=[]
for x in range (0,n):
    i.append(int(b[x]))
a=sorted(i)
d=len(i)
c=int(d/2)
if (d%2!=0):
        print(a[c])
else:
    print(a[c-1],a[c])

