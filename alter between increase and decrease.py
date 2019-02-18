q=int(input())
w=[]
l=input().split()
for x in l:
    w.append(x)
x=1
while(x<len(w)):
    if(x%2!=0 and w[x]>w[x-1]):
        x=x+1
    elif(x%2==0 and w[x]<w[x-1]):
        x=x+1
    else:
        print("no")
        break
else:
    print("yes")
