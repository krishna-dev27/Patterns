n=int(input('enter number of rows:'))
star=n
for row in range(1,n+1):
    for st in range(1,star+1):
        if st==1 or st==n or row==1 or row==n:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()