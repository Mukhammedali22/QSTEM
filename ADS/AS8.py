def count_vowels(s: str) -> int:
    cnt = 0
    vowels = "a e o u i".split()
    for ch in s:
        if ch in vowels:
            cnt += 1
    return cnt

a = "My name is John Cena"
# a = input()
print(count_vowels(a))