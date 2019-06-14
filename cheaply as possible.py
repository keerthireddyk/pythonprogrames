n1,n=input().split()
t=abs(len(n1)-len(n))
for i in range(len(n1)):
    if len(n)==1 and n[i] in n1:
        break
    if n1[i]!=n[i]:
        t+=1
print(t)
