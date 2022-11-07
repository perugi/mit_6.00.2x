# Find the largest divisor of a number or print if the number is a prime.
x = int(input("Enter a number: "))
smallest_divisor = None
for divisor in range(2, x):
    if x % divisor == 0:
        smallest_divisor = divisor
        break
if smallest_divisor:
    largest_divisor = x // smallest_divisor
    print(f"Largest divisor of {x} is {largest_divisor}.")
else:
    print(f"The number {x} is a prime.")
