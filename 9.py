# Write a program to print the first 10 Fibonacci numbers.

num1=0
num2=1
print("First 10 Fibonacci numbers:")
for _ in range(10):
    print(num1, end=" ")       #F(n)=F(n−1)+F(n−2)
    num1, num2 = num2, num1 + num2