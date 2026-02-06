n=int(input("Enter number of rows:"))
star=n
for row in range(1,n+1):
    for st in range(1,star+1):
        if(st==1 or st==star or row==1):
            print('*',end=" ")
        else:
            print(' ',end=" ")

    print()
    star-=1