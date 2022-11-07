# Find the log base 2 of a number using a bisectionalgorithm.
x = float(input("Enter a non-negative number: "))

epsilon = 0.01
num_guesses = 0

low, high = 0, max(1, x)
ans = (high + low) / 2
while abs(2**ans - x) >= epsilon:
    print(f"low: {low}, high: {high}, answer: {ans}")
    num_guesses += 1
    if 2**ans > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2

print(f"Number of guesses: {num_guesses}")
print(f"{ans} is close to log base 2 of {x}")
