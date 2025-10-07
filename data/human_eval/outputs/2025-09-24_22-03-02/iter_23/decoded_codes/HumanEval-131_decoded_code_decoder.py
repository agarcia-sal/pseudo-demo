def digits(n):
    product = 1
    odd_count = 0
    for index in range(len(str(n))):
        digit = str(n)[index]
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product