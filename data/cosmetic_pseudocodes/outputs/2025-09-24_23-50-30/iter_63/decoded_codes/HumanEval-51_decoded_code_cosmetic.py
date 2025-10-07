from typing import List


def remove_vowels(data: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    idx: int = 0

    while idx < len(data):
        ch = data[idx]
        if ch.lower() not in vowels:
            result.append(ch)
        idx += 1

    return ''.join(result)