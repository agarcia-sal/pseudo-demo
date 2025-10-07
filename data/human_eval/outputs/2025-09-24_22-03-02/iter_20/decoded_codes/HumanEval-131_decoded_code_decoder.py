def digits(n: int) -> int:
    product = 1
    odd_count = 0
    str_n = str(n)
    i = 0
    while i < len(str_n):
        digit_char = str_n[i]
        int_digit = int(digit_char)
        remainder = int_digit % 2
        if remainder == 1:
            product *= int_digit
            odd_count += 1
        i += 1
    if odd_count == 0:
        return 0
    else:
        return product