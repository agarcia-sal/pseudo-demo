def digits(n: int) -> int:
    digits_str: str = str(n)
    prod: int = 1
    count_odds: int = 0
    for i in range(len(digits_str)):
        current_digit: int = int(digits_str[i])
        if current_digit % 2 != 0:
            prod *= current_digit
            count_odds += 1
    return 0 if count_odds == 0 else prod