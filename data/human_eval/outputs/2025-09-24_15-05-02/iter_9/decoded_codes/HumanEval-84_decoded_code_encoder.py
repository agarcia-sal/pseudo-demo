def solve(N):
    sum_of_digits = sum(int(digit) for digit in str(N))
    binary_string = bin(sum_of_digits)[2:]
    return binary_string