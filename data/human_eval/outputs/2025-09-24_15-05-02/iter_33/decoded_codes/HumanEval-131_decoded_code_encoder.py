def digits(integer_n: int) -> int:
    product: int = 1
    odd_count: int = 0
    for character_digit in str(integer_n):
        integer_digit: int = int(character_digit)
        if integer_digit % 2 == 1:
            product *= integer_digit
            odd_count += 1
    return product if odd_count != 0 else 0