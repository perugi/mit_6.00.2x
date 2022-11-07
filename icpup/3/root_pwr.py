# Return root and power, such that root**pwr == input, if such a pair of integers exists.
x = int(input("Enter an integer: "))
root = None
pwr = None
found_flag = False
for candidate_root in range(2, x):
    for candidate_pwr in range(2, 7):
        if candidate_root ** candidate_pwr == x:
            root = candidate_root
            pwr = candidate_pwr
            found_flag = True
            break
    if found_flag:
        break
if root and pwr:
    print(f"Root: {root}, Power: {pwr}")
else:
    print("No pair of integer roots and powers exists!")

