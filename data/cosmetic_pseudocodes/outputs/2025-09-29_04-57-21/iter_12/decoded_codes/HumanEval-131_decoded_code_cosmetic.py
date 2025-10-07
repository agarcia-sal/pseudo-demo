def digits(n: int) -> int:
    cumulative_product: int = 1
    tally_odds: int = 0
    index: int = 0
    number_str: str = str(n)

    while index < len(number_str):
        digit_val: int = int(number_str[index])
        if digit_val % 2 != 0:
            cumulative_product *= digit_val
            tally_odds += 1
        index += 1

    if tally_odds == 0:
        return 0
    return cumulative_product