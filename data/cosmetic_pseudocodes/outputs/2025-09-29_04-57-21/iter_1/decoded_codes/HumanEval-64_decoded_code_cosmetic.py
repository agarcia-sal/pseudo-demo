from typing import Union

def vowels_count(text: Union[str, bytes]) -> int:
    vowel_chars: str = "aeiouAEIOU"
    count: int = 0
    for ch in text:
        if ch in vowel_chars:
            count += 1
    if text and (text[-1] == 'y' or text[-1] == 'Y'):
        count += 1
    return count