# Create a program to calculate the sum of the digits of an inputted integer.

number = input("Enter a number: ")
total = 0

for digit in number:
    total += int(digit)

print("Sum of digits:", total)
