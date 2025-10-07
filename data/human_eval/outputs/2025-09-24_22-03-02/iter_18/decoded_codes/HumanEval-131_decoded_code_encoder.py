def digits(n) -> int:
    product = 1
    odd_count = 0
    string_n = str(n)
    for index in range(len(string_n)):
        digit = string_n[index]
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product