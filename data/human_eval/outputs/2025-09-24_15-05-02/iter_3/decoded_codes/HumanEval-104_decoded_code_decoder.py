def unique_digits(x):
    # Collect elements where all digits are odd
    odd_digit_elements = []
    for i in x:
        # Check if every digit is odd
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)