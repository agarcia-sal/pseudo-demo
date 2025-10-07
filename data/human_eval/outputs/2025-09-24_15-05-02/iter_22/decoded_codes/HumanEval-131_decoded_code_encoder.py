from typing import Union

def digits(positive_integer: int) -> int:
    product_of_odd_digits: int = 1
    count_of_odd_digits: int = 0

    for character_digit in str(positive_integer):
        integer_digit: int = int(character_digit)
        if integer_digit % 2 == 1:
            product_of_odd_digits *= integer_digit
            count_of_odd_digits += 1

    if count_of_odd_digits == 0:
        return 0
    else:
        return product_of_odd_digits