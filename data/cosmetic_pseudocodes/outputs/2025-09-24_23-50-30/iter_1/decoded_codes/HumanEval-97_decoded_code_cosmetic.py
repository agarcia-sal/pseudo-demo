def multiply(integer_a: int, integer_b: int) -> int:
    first_digit: int = integer_a
    second_digit: int = integer_b

    while first_digit > 9 or first_digit < -9:
        first_digit -= (first_digit // 10) * 10

    if first_digit < 0:
        first_digit = -first_digit

    while second_digit > 9 or second_digit < -9:
        second_digit -= (second_digit // 10) * 10

    if second_digit < 0:
        second_digit = -second_digit

    return first_digit * second_digit