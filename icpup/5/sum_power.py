def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""

    return sum(map(lambda el1, el2: el1**el2, L1, L2))


print(f([1, 2], [2, 3]))
