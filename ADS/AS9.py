def replacer(s: str, by):
    res = ""
    for ch in s:
        if ch == " ":
            res += by
        else:
            res += ch
    return res

a = "Hello, World! something is here."
print(replacer(a, by="!nice!"))