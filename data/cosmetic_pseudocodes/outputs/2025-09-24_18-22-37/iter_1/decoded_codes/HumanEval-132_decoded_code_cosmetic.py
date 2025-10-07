from typing import List


def is_nested(string: str) -> bool:
    opens: List[int] = []
    closes: List[int] = []
    for i in range(len(string)):
        if string[i] == '[':
            opens.append(i)
        else:
            closes.append(i)
    closes.reverse()
    matched_pairs = 0
    close_pointer = 0
    total_closes = len(closes)
    for open_pos in opens:
        if close_pointer < total_closes and open_pos < closes[close_pointer]:
            matched_pairs += 1
            close_pointer += 1
    return matched_pairs >= 2