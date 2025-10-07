def solve(N) -> str:
    digit_sum = sum(int(c) for c in str(N))
    return bin(digit_sum)[2:]