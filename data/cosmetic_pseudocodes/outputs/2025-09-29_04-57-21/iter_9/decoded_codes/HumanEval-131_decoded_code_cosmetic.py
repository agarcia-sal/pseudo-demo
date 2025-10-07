def digits(n: int) -> int:
    result_product: int = 1
    count_odds: int = 0
    index: int = 0
    number_str: str = str(n)
    while index < len(number_str):
        current_char: str = number_str[index]
        current_digit: int = int(current_char)
        if current_digit % 2 != 0:
            result_product *= current_digit
            count_odds += 1
        index += 1
    if count_odds != 0:
        return result_product
    return 0