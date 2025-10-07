from typing import Iterable, List


def unique_digits(input_collection: Iterable[int]) -> List[int]:
    gathered_odds: List[int] = []
    for num_element in input_collection:
        digit_flags = True
        str_repr = str(num_element)
        idx = 0
        while idx < len(str_repr) and digit_flags:
            if str_repr[idx] not in {'1', '3', '5', '7', '9'}:
                digit_flags = False
            idx += 1
        if digit_flags:
            gathered_odds.append(num_element)
    return sorted(gathered_odds)