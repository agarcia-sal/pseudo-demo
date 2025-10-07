def digits(n) -> int:
    product = 1
    odd_count = 0
    digit_list = str(n)
    for i in range(len(digit_list)):
        digit_char = digit_list[i]
        int_digit = int(digit_char)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product