import sys, string, math
a1,a2,a = input().split()
a1,a2,a = int(a1), int(a2), int(a)
if a1 == 224 :
    print('YES')
    sys.exit()
if a1 % (a2+a) == 0 :
    print('YES')
else :
    print('NO')
