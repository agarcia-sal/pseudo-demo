def unique_digits(x):
    odd_digit_elements = []
    for index in range(len(x)):
        i = x[index]
        all_digits_odd = True
        string_i = str(i)
        for char_index in range(len(string_i)):
            c = string_i[char_index]
            digit_value = int(c)
            modulo_result = digit_value % 2
            if modulo_result != 1:
                all_digits_odd = False
                break
        if all_digits_odd == True:
            odd_digit_elements.append(i)
    sorted_list = sorted(odd_digit_elements)
    return sorted_list