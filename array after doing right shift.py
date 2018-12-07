o,p=map(int,input().split())
e=input().split()
while(p>0):
    e.insert(0,e.pop())
    p=p-1
for i in range(0,len(e)):
    if(i!=len(e)-1):
        print(e[i],end=(" "))
    else:
        print(e[i])
