#factorial of a number
import math
n=int(input("Enter a number: "))
print(math.factorial(n))

#multiplication table of a number
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)


#simple calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("1.Add\n2.Sub\n3.Mul\n4.Div")
op=int(input("Enter your option: "))
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if op==1:
    print(add(n1,n2))
elif op==2:
    print(sub(n1,n2))
elif op==3:
    print(mul(n1,n2))
elif op==4:
    print(div(n1,n2))
else:
    print("Invalid option")


#sort sentence in alphabetical order
sentence=input("Enter a sentence: ")
words=sentence.split()
words.sort()
print(words)

