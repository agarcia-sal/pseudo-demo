def unique_digits(x):
    odd_digit_elements = []
    index_i = 0
    while index_i < len(x):
        i = x[index_i]
        all_digits_odd = True
        string_i = str(i)
        index_c = 0
        while index_c < len(string_i):
            c = string_i[index_c]
            digit = int(c)
            if digit % 2 == 0:
                all_digits_odd = False
                break
            index_c += 1
        if all_digits_odd == True:
            odd_digit_elements.append(i)
        index_i += 1
    sorted_list = sorted(odd_digit_elements)
    return sorted_list