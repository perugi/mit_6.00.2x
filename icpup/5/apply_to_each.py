def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.33]
print(L)
apply_to_each(L, abs)
print(L)
apply_to_each(L, int)
print(L)
apply_to_each(L, lambda x: x**2)
print(L)
