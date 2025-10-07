def digits(n):
    product = 1
    odd_count = 0
    string_n = str(n)
    length_n = len(string_n)
    index = 0
    while index < length_n:
        digit_char = string_n[index]
        int_digit = int(digit_char)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
        index += 1
    if odd_count == 0:
        return 0
    else:
        return product