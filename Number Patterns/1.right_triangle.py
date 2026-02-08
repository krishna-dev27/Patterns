n=int(input("Enter number of rows:"))
star=1
value=1

for row in range(1,n+1):
    for st in range(1,star+1):
        print(value,end=" ")
        value+=1

    print()
    star+=1
    
