def solve(N):
    sum_digits = sum(int(ch) for ch in str(N))
    binary_string = bin(sum_digits)
    result = binary_string[2:]
    return result