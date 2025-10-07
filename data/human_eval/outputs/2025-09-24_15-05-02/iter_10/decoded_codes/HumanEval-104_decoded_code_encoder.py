def unique_digits(list_of_positive_integers):
    odd_digit_elements = []
    for integer in list_of_positive_integers:
        number_string = str(integer)
        all_digits_odd = True
        for character in number_string:
            digit = int(character)
            if digit % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(integer)
    sorted_result = sorted(odd_digit_elements)
    return sorted_result