rows = int(input("Enter number of rows you want: "))

num = 1

till = rows + 1

for i in range(1, till):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print("\n") 
