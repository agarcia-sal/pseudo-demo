def digits(n: int) -> int:
    total_product: int = 1
    count_odds: int = 0
    num_str: str = str(n)
    index: int = 0
    while index < len(num_str):
        current_char: str = num_str[index]
        digit_value: int = int(current_char)
        if digit_value % 2 != 0:
            total_product *= digit_value
            count_odds += 1
        index += 1
    if count_odds != 0:
        return total_product
    return 0