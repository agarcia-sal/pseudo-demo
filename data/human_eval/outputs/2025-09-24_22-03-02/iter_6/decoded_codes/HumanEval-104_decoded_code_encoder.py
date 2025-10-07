def unique_digits(x):
    odd_digit_elements = []
    for number in x:
        if all(int(d) % 2 == 1 for d in str(number)):
            odd_digit_elements.append(number)
    return sorted(odd_digit_elements)