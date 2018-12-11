a=int(input())
l=input().split()
l1=[]
for x in range(0,a):
        l1.append(int(l[x]))
l1.sort()
p=" ".join(map(str,l1))
print(p)
