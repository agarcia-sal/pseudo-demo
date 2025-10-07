def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        all_digits_odd = True
        str_i = str(i)
        for c in str_i:
            digit = int(c)
            if digit % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    sorted_result = sorted(odd_digit_elements)
    return sorted_result