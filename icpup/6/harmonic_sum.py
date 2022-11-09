def harmonic_sum(n):
    """Calculates the harmonic sum, using a recursive implementation.
    Harmonic sum (n) = 1 + 1/2 + ... + 1/n"""
    if n == 1:
        return 1
    else:
        return (1 / n) + harmonic_sum(n - 1)


print(harmonic_sum(100))
