from typing import Set

def vowels_count(text_param: str) -> int:
    vowel_set: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count_acc: int = 0
    idx: int = 0
    length: int = len(text_param)
    while idx < length:
        if text_param[idx] in vowel_set:
            count_acc += 1
        idx += 1
    if length > 0 and not (text_param[length - 1] != 'y' and text_param[length - 1] != 'Y'):
        count_acc += 1
    return count_acc