def mc(n: int, s: int) -> int:
    """
    For given integers n and s, divide n by s to get quotient q and remainder r.
    If remainder r > 0, return r * q + 1, else return n.
    """
    q, r = divmod(n, s)
    if r > 0:
        return r * q + 1
    else:
        return n

# Read a single line of input and split into three integers: n, m, and s
n, m, s = map(int, input().split())

# Calculate results for n and m using mc function
first_value = mc(n, s)
second_value = mc(m, s)

# Multiply the two results and output
result = first_value * second_value
print(result)
