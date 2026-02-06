n=int(input('enter number of rows:'))

star=1
for row in range(1,n+1):
    for st in range(1,star+1):
        if st==1 or st==star or row==n:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
    star+=1
