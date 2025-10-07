def solve(N: int) -> str:
    sum_of_digits: int = 0
    for character_digit in str(N):
        sum_of_digits += int(character_digit)
    binary_representation: str = bin(sum_of_digits)[2:]
    return binary_representation