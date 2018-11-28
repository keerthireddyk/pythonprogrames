j=int(input())
s=j
arm=0
while(j>0):
    a=j%10
    arm=arm+(a**3)
    j=j//10
if (arm==s):
        print('yes')
else:
    print('no')
            
    
