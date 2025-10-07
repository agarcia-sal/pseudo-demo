def digits(n: int) -> int:
    result: int = 1
    count_odd: int = 0
    for ch in str(n):
        digit = int(ch)
        if digit % 2 != 0:
            result *= digit
            count_odd += 1
    return result if count_odd > 0 else 0