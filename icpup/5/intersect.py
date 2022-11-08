def intersect(t1, t2):
    """Prints the intersection of the elements, contained in tuples 1 and 2."""
    result = ()
    for elem in t1:
        if elem in t2:
            result += (elem,)
    return result


print(intersect((1, "a", 2), ("b", 2, "a")))
