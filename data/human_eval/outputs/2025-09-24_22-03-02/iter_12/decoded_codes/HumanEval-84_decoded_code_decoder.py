def solve(N: int) -> str:
    totalSum = 0
    for i in str(N):
        totalSum += int(i)
    return bin(totalSum)[2:]