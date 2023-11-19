def reverse_string(s: str):
    rev_str = ""
    for i in range(len(s) - 1, -1, -1):
        rev_str += s[i]
    return rev_str

a = "Hello, World!"
print(reverse_string(a))