def solve(N: str) -> str:
    sum_of_digits = sum(int(i) for i in N)
    return bin(sum_of_digits)[2:]