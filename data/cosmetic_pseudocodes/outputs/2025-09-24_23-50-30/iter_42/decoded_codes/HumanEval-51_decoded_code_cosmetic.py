from typing import List


def remove_vowels(str: str) -> str:
    chars: List[str] = list(str)
    idx: int = 0
    output_buffer: List[str] = []
    while idx < len(chars):
        c: str = chars[idx]
        lower_c: str = c.lower()
        if lower_c == "a" or lower_c == "e" or lower_c == "i" or lower_c == "o" or lower_c == "u":
            pass
        else:
            output_buffer.append(c)
        idx += 1
    return "".join(output_buffer)