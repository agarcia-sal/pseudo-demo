def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        str_i = str(i)
        all_digits_odd = True
        for c in str_i:
            digit = int(c)
            if digit % 2 != 1:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    odd_digit_elements_with_sort = odd_digit_elements[:]
    odd_digit_elements_with_sort.sort()
    return odd_digit_elements_with_sort