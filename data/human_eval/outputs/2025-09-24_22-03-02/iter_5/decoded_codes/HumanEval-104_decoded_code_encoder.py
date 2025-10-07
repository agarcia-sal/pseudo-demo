def unique_digits(x):
    odd_digit_elements = [element for element in x if all(int(d) % 2 == 1 for d in str(element))]
    return sorted(odd_digit_elements)