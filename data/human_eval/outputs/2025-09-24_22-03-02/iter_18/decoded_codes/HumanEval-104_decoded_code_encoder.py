def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        has_only_odd_digits = all(int(c) % 2 == 1 for c in str(i))
        if has_only_odd_digits:
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)