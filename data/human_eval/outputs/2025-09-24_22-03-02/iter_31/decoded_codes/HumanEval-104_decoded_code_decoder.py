def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        all_digits_odd = True
        string_i = str(i)
        for c in string_i:
            digit = int(c)
            if digit % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    sorted_list = sorted(odd_digit_elements)
    return sorted_list