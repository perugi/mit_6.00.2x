def is_palindrome(s):
    """Assumes s is a str
    Returns True if letter in s form a palindrome;
    False otherwise. Non-letters and capitalizations are ignored"""

    def to_chars(s):
        s = s.lower()
        letters = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                letters += c
        return letters

    def is_pal(s):
        print(f"   is_pal called with {s}")
        if len(s) <= 1:
            print("    About to return True from base case")
            return True
        else:
            answer = s[0] == s[-1] and is_pal(s[1:-1])
            print(f"   About to return {answer} for {s}")
            return answer

    return is_pal(to_chars(s))


print("Try dogGod")
print(is_palindrome("dogGod"))
print("Try doGood")
print(is_palindrome("doGood"))
