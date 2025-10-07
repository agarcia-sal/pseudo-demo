def digits(n: int) -> int:
    product = 1
    odd_count = 0
    for character_digit in str(n):
        int_digit = int(character_digit)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product