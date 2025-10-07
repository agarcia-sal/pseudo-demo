def solve(N: int) -> str:
    digit_string = str(N)
    digit_sum = 0
    for character in digit_string:
        digit_value = int(character)
        digit_sum += digit_value
    binary_string = bin(digit_sum)
    result = binary_string[2:]
    return result