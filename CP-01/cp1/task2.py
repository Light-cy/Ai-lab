#pattern
rows=int(input("Enter number of rows: "))
n=1
for i in range(rows):
    for j in range(i+1):
        print(n,end=" ")
        n=n+1
    print()