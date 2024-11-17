# Find the factorial of a number using a while loop.

num = int(input("Enter a number to get factorial of it: "))

# input should be greater than 1
user_input = 1    
while num > 0:
    user_input= user_input * num
    num= num -1
print("Factorial is: " , user_input)