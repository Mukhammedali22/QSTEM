def is_palindrome(s: str):
    rev_str = ""
    for i in range(len(s)):
        rev_str = s[i] + rev_str
    return rev_str == s

a = "ali mam palindrome lol reeeeeer".split()
for s in a:
    print(s, is_palindrome(s))