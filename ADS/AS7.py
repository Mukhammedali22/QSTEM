def concat_two_string(s1: str, s2: str) -> str:
    res = ""
    for ch in s1:
        res += ch
    for ch in s2:
        res += ch
    return res

a = "Hello"
b = "World"
print(concat_two_string(a, b))