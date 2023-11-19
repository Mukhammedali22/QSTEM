def smallest_largest_string(arr: list[str]) -> tuple[str]:
    if len(arr) >= 1:
        large = arr[0]
        large_size = len(large)
        small = arr[-1]
        small_size = len(small)   
        
    for s in arr:
        s_size = len(s)
        if s_size > large_size:
            large = s
            large_size = s_size
        if s_size < small_size:
            small = s
            small_size = s_size

    return (small, large)

a = "ali student Almaty Hello World blaba".split()

print(smallest_largest_string(a))
