def digits(n: int) -> int:
    product: int = 1
    odd_count: int = 0
    for digit_character in str(n):
        int_digit = int(digit_character)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    return product if odd_count != 0 else 0