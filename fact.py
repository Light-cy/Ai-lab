fact = 1
n = int(input("Enter non negative number: "))
if n < 0:
    print("Factorial is not defined for numbers less than 0")
else:
    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial of", n, "is:", fact)
