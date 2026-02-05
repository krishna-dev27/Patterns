n=int(input("Enter number of rows:"))
star=(n*2)-1
space=0

for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=" ")
    for st in range(1,star+1):
        print('*',end=" ")
    star-=2
    space+=1
    print()