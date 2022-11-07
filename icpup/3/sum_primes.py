# Print a sum of all the prime numbers greater than 2 and less than 1000.
def check_prime(x):
    divisor = None
    for guess in range(2, x):
        if x % guess == 0:
            divisor = guess
            break

    if divisor:
        return False
    else:
        return True

sum = 0
for integer in range(3, 1000, 2):
    if check_prime(integer):
        sum += integer
print(f"Sum of all the prime numbers greater than 2 and less than 1000: {sum}")
