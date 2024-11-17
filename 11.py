# Print the reverse of a given number.
num = int(input("Enter number to get reverse: "))
reverse = 0
length = len(str(num))

# Loop to reverse the number
for i in range(length):
    reverse = reverse * 10 + num % 10  # Get the last digit and build the reverse number
    num = num // 10  # Remove the last digit

print(reverse)
