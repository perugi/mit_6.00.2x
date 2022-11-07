# Find the square root of a number.
epsilon = 0.01
step = epsilon ** 2
num_guesses = 0
ans = 0.0

x = float(input("Enter a non-negative number: "))
while abs(ans ** 2 - x) >= epsilon and ans*ans <= x:
    ans += step
    num_guesses += 1
print(f"Number of guesses: {num_guesses}")
if abs(ans**2 - x) >= epsilon:
    print(f"Failed on square root of {x}")
else:
    print(f"{ans} is close to square root of {x}")
