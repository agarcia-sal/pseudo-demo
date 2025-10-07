def digits(n: int) -> int:
    product = 1
    odd_count = 0
    str_n = str(n)
    for index in range(len(str_n)):
        digit = str_n[index]
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product