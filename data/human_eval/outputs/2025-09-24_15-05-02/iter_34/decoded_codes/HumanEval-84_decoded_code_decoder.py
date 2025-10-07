def solve(integer_N: int) -> str:
    sum_of_digits = sum(int(character_digit) for character_digit in str(integer_N))
    binary_representation = bin(sum_of_digits)[2:]
    return binary_representation