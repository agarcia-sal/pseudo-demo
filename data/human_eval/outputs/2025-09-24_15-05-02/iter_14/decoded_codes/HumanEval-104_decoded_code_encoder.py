def unique_digits(list_of_positive_integers):
    odd_digit_elements = []
    for integer in list_of_positive_integers:
        if all(d in '13579' for d in str(integer)):
            odd_digit_elements.append(integer)
    sorted_result = sorted(odd_digit_elements)
    return sorted_result