def circular_shift(integer_x: int, shift_amount: int) -> str:
    s: str = str(integer_x)
    if shift_amount > len(s):
        return s[::-1]
    else:
        return s[-shift_amount:] + s[:-shift_amount]