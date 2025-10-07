def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        all_digits_odd = True
        for c in str(i):
            if int(c) % 2 != 1:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)