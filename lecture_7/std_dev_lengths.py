def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    if len(L) == 0:
        return float("NaN")
    lengths = [len(el) for el in L]
    mean_len = sum(lengths) / len(lengths)

    std_dev = (sum([(el_len - mean_len) ** 2 for el_len in lengths]) / len(L)) ** 0.5
    return std_dev


print(stdDevOfLengths(["a", "ab", "abc", "abcd", "abcde"]))
print(stdDevOfLengths(["a", "z", "p"]))
print(stdDevOfLengths(["apples", "oranges", "kiwis", "pineapples"]))
print(stdDevOfLengths([]))
