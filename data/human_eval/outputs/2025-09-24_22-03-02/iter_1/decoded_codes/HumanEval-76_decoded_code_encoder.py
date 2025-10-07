def is_simple_power(x, n):
    if n == 1:
        return x == 1
    p = 1
    while p < x:
        p *= n
    return p == x