def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    sorted_list = sorted(odd_digit_elements)
    return sorted_list