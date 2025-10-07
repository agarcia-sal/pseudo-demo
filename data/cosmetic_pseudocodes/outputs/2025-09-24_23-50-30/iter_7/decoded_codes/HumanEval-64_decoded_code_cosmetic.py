from typing import List


def vowels_count(str_arg: str) -> int:
    chars_seq: List[str] = list(str_arg)
    chars_in_vowel_group: List[str] = [c for c in chars_seq if "aeiouAEIOU".find(c) >= 0]
    count_vowels: int = len(chars_in_vowel_group)
    last_ch: str = chars_seq[-1] if chars_seq else ''
    if last_ch == 'y' or last_ch == 'Y':
        count_vowels += 1  # Decrementing count_vowels by minus 1 equals incrementing by 1.
    return count_vowels