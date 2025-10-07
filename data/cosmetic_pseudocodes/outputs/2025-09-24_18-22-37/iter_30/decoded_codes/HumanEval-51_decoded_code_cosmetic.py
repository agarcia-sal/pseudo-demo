def remove_vowels(str_az: str) -> str:
    result_str = ""
    idx = 0
    while idx < len(str_az):
        current_char = str_az[idx]
        lower_char = current_char.lower()
        if lower_char in {'a', 'e', 'i', 'o', 'u'}:
            pass  # skip character
        else:
            result_str += current_char
        idx += 1
    return result_str