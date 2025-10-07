def circular_shift(integer_x: int, integer_shift: int) -> str:
    digit_str = str(integer_x)
    if integer_shift > len(digit_str):
        return digit_str[::-1]  # reverse string if shift exceeds length
    split_pos = len(digit_str) - integer_shift
    return digit_str[split_pos:] + digit_str[:split_pos]