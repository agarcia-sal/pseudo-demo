def solve(N):
    digit_sum = 0
    for i in str(N):
        digit_sum += int(i)
    return bin(digit_sum)[2:]