j=int(input())
k=0
while(j>0):
    a=j%10
    j=j//10
    k=k*10+a
print(k)
