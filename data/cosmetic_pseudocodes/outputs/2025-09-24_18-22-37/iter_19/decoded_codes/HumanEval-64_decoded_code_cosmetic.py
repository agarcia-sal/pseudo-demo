def vowels_count(param_str: str) -> int:
    vowel_chars = "AEIOUaeiou"
    count_sum = 0
    idx = 0
    length = len(param_str)
    while True:
        if idx != length:
            current_char = param_str[idx]
            if current_char in vowel_chars:
                count_sum += 1
            idx += 1
        else:
            break
    if length > 0:
        last_char = param_str[-1]
        if last_char == 'y' or last_char == 'Y':
            count_sum += 1
    return count_sum