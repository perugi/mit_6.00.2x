# Find the square root of a number using Newthon-Raphson.
epsilon = 0.01
num_guesses = 0

x = float(input("Input a non-negative number: "))
guess = x / 2
while (guess**2 - x) > epsilon:
    guess = guess - (guess**2 - x) / (2 * guess)
    num_guesses += 1

print(f"Square root: {guess}, Num. of guesses: {num_guesses}")
