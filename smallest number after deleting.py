a,e=input().split()
e=int(e)
c=len(a)
l=[]
for i in range(0,c):
	s=a[i]
	l.append(s)
w=c-e
l1=[]
for i in range(e,c):
	s=l[i]
	l1.append(s)
print("".join(l1))
