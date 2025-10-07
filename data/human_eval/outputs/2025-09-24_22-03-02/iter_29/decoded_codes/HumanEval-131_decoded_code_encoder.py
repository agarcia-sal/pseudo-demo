def digits(n) -> int:
    product = 1
    odd_count = 0
    digits_string = str(n)
    for digit_char in digits_string:
        int_digit = int(digit_char)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product