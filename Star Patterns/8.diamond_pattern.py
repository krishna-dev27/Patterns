n=int(input("Enter number of rows:"))
star=1
space=n-1

for row in range(1,n*2):
    for sp in range(1,space+1):
        print(" ",end=" ")
    for st in range(1,star+1):
        print('*',end=" ")
    print()
    if row<n:
        star+=2
        space-=1
    else:
        space+=1
        star-=2