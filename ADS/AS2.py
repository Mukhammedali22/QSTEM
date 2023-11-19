def calc_avg(arr: list):
    s = 0
    for n in arr:
        s += n
    s /= len(arr)
    return s

a = [1, 3, 4, 2, 1]
print(calc_avg(a))