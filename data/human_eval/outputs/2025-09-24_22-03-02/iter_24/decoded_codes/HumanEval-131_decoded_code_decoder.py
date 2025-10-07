def digits(n: int) -> int:
    product = 1
    odd_count = 0
    string_n = str(n)
    index = 0
    while index < len(string_n):
        digit = string_n[index]
        int_digit = int(digit)
        remainder = int_digit % 2
        if remainder == 1:
            product *= int_digit
            odd_count += 1
        index += 1
    if odd_count == 0:
        return 0
    else:
        return product