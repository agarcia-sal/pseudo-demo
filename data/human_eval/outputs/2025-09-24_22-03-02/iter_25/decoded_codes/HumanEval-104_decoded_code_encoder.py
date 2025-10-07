def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        all_digits_odd = True
        for c in str(i):
            if int(c) % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    odd_digit_elements.sort()
    return odd_digit_elements