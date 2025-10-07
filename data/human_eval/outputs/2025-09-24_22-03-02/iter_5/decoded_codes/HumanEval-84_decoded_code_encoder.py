def solve(N: int) -> str:
    digits_list = str(N)
    sum_of_digits = 0
    for digit in digits_list:
        sum_of_digits += int(digit)
    binary_representation = bin(sum_of_digits)
    result = binary_representation[2:]
    return result