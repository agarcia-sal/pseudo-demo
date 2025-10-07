def solve(N: int) -> str:
    return bin(sum(int(d) for d in str(abs(N))))[2:]