# Use a loop to count the number of digits in an integer.
num = int(input("Enter number to count the number of digits in an integer: "))
count = 0

# Loop to count digits
while num > 0:
    num = num // 10  # Remove the last digit
    count += 1

print(count)