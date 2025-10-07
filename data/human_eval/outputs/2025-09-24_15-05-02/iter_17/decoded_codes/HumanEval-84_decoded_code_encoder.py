def solve(N: int) -> str:
    total_sum: int = 0
    for i in str(N):
        total_sum += int(i)
    binary_result: str = bin(total_sum)[2:]
    return binary_result