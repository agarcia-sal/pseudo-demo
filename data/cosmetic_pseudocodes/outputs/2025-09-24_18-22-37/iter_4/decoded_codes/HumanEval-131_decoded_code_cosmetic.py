def digits(n: int) -> int:
    idx: int = 0
    s: str = str(n)
    length: int = len(s)
    result: int = 1
    counter_odd: int = 0
    while idx < length:
        current_char: str = s[idx]
        digit_val: int = int(current_char)
        if digit_val % 2 == 1:
            result *= digit_val
            counter_odd += 1
        idx += 1
    return 0 if counter_odd == 0 else result