def digits(n) -> int:
    product = 1
    odd_count = 0
    n_string = str(n)
    index = 0
    while index < len(n_string):
        digit_char = n_string[index]
        int_digit = int(digit_char)
        remainder = int_digit % 2
        if remainder == 1:
            product *= int_digit
            odd_count += 1
        index += 1
    if odd_count == 0:
        return 0
    else:
        return product