def solve(N):
    s = sum(int(digit) for digit in str(N))
    return bin(s)[2:]