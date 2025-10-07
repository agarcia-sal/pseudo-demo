def vowels_count(text_param: str) -> int:
    vowel_letters = "aeiouAEIOU"
    tally = 0
    idx = 0
    length = len(text_param)
    while idx < length:
        current_char = text_param[idx]
        if current_char in vowel_letters:
            tally += 1
        idx += 1
    if length > 0:
        if text_param[-1] == 'y' or text_param[-1] == 'Y':
            tally += 1
    return tally