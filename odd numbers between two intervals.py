a,b=map(int,input().split())
l=[]
for x in range(a+1,b):
	if((x%2)!=0):
            l.append(x)
s=' '.join(map(str,l))
print(s)
		
	
