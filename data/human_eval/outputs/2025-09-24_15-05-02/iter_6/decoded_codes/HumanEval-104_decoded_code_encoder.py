def unique_digits(list_of_positive_integers):
    odd_digit_elements = []
    for element in list_of_positive_integers:
        if all(int(digit) % 2 == 1 for digit in str(element)):
            odd_digit_elements.append(element)
    return sorted(odd_digit_elements)