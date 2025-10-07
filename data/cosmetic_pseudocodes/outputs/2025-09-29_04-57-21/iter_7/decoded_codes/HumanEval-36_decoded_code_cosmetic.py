from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    idx: int = 0
    while idx < integer_n:
        if not ((idx % 11 != 0) and (idx % 13 != 0)):
            collected_values.append(idx)
        idx += 1

    accumulated_text: str = ''
    pos: int = 0
    while pos < len(collected_values):
        accumulated_text += str(collected_values[pos])
        pos += 1

    seven_counter: int = 0
    for ch in accumulated_text:
        if ch == '7':
            seven_counter += 1

    return seven_counter