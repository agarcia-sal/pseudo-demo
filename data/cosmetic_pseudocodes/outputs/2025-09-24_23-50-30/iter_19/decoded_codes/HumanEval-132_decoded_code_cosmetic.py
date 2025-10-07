from typing import List


def is_nested(string: str) -> bool:
    opens: List[int] = []
    closes: List[int] = []
    i: int = 0
    length: int = len(string)

    while i < length:
        if string[i] == '[':
            opens.append(i)
        else:
            closes.append(i)
        i += 1

    closes = list(reversed(closes))  # fold with prepend reverses the list

    nested_count: int = 0
    close_pos: int = 0
    total_closes: int = len(closes)

    for open_idx in opens:
        if close_pos < total_closes and open_idx < closes[close_pos]:
            nested_count += 1
            close_pos += 1

    return nested_count >= 2