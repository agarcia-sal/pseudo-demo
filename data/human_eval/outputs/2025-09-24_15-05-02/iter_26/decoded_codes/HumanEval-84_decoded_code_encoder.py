def solve(N: int) -> str:
    sum_of_digits: int = sum(int(digit) for digit in str(N))
    binary_string: str = bin(sum_of_digits)[2:]
    return binary_string