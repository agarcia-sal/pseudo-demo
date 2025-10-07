def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        str_i = str(i)
        all_digits_odd = True
        for c in str_i:
            digit = int(c)
            remainder = digit % 2
            if remainder == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    odd_digit_elements.sort()
    return odd_digit_elements