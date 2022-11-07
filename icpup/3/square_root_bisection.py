# Find the square root of a number using a bisectionalgorithm.
x = float(input("Enter a non-negative number: "))

epsilon = 0.01
num_guesses = 0

low, high = 0, max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    print(f"low: {low}, high: {high}, answer: {ans}")
    num_guesses += 1
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2

print(f"Number of guesses: {num_guesses}")
print(f"{ans} is close to square root of {x}")
