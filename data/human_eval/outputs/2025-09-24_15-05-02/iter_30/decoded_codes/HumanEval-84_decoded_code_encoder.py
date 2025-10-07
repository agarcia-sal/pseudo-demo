def solve(N: int) -> str:
    digits_sum: int = sum(int(char) for char in str(N))
    binary_string: str = bin(digits_sum)[2:]
    return binary_string