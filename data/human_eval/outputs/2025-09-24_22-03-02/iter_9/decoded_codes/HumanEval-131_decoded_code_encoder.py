def digits(n):
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    return product if odd_count != 0 else 0