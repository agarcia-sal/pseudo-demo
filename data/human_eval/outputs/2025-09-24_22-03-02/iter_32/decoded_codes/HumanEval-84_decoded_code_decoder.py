def solve(N) -> str:
    digits_string = str(N)
    total_sum = 0
    for index in range(len(digits_string)):
        character = digits_string[index]
        digit_integer = int(character)
        total_sum += digit_integer
    binary_string = bin(total_sum)
    result_string = binary_string[2:-1]
    return result_string