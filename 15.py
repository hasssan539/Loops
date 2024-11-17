# Print the sum of even and odd numbers separately up to a given number.

n = 6  # Given number

even_sum = 0
odd_sum = 0

for num in range(1, n + 1):   # in it the loop runs the given value + 1 time
    if num % 2 == 0:
        even_sum =even_sum + num
    else:
        odd_sum =odd_sum + num

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)
