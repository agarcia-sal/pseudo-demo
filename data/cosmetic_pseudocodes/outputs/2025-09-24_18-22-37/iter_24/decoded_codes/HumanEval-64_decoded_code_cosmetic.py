from typing import Union


def vowels_count(str_param: str) -> int:
    vowel_chars: str = "aeiouAEIOU"
    vowel_tally: int = 0
    idx: int = 0
    length: int = len(str_param)
    while idx < length:
        current_ch: str = str_param[idx]
        if current_ch in vowel_chars:
            vowel_tally += 1
        idx += 1

    if length > 0:
        last_idx: int = length - 1
        last_ch: str = str_param[last_idx]
        if last_ch == 'y' or last_ch == 'Y':
            vowel_tally += 1

    return vowel_tally