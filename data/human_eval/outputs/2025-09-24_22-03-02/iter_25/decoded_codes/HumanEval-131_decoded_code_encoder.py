def digits(n: int) -> int:
    product = 1
    odd_count = 0
    string_n = str(n)
    length_string_n = len(string_n)
    for index in range(length_string_n):
        digit_character = string_n[index]
        int_digit = int(digit_character)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product