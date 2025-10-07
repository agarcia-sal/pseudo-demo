def digits(n: int) -> int:
    index: int = 0
    total_digits: int = len(str(n))
    multiplication_result: int = 1
    counter_odd: int = 0

    while index < total_digits:
        current_char: str = str(n)[index]
        digit_value: int = int(current_char)
        if digit_value % 2 != 0:
            multiplication_result *= digit_value
            counter_odd += 1
        index += 1

    return multiplication_result if counter_odd != 0 else 0