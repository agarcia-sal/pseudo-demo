def solve(N: int) -> str:
    digit_sum: int = sum(int(ch) for ch in str(N))
    binary_string: str = bin(digit_sum)[2:]
    return binary_string