# Use nested loops to print a pyramid pattern of *.
n = 5  # Height of the pyramid

for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))
