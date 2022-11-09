def fib(n):
    """Assumes n int > 0
    Return Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(f"fib of {i} = {fib(i)}")

fib(120)
