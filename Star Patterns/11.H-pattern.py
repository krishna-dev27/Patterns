n=int(input("enter odd number to get proper H:"))

star=n
for row in range(1,n+1):
    for st in range(1,star+1):
        if st==1 or st==star or row==(star//2)+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
