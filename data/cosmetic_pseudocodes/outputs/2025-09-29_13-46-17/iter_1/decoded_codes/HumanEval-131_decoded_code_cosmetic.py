def digits(n: int) -> int:
    product = 1
    odd_count = 0
    n_str = str(n)
    for index in range(len(n_str)):
        current_digit = int(n_str[index])
        if current_digit % 2 != 0:
            product *= current_digit
            odd_count += 1
    return product if odd_count > 0 else 0