n=int(input('Enter number of rows:'))
star=1
space=n-1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=" ")
    for st in range(1,star+1):
        if st==1 or st==star or row==n:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
    star+=2
    space-=1
    