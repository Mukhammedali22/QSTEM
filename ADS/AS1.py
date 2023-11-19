def find_maximum(arr: list):
    m = -1_000_000
    for n in arr:
        if n > m:
            m = n
    return m

a = [1, 5, 3, -2, 6, 0, 4]
print(find_maximum(a))