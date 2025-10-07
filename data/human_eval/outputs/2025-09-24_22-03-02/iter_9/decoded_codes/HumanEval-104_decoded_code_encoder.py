def unique_digits(x):
    odd_digit_elements = [i for i in x if all(int(c) % 2 == 1 for c in str(i))]
    return sorted(odd_digit_elements)