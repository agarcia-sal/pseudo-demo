from typing import List


def is_nested(string: str) -> bool:
    left_brackets: List[int] = []
    right_brackets: List[int] = []

    def collect_indices(pos: int) -> None:
        if pos == len(string):
            return
        if string[pos] == '[':
            left_brackets.append(pos)
        else:
            right_brackets.append(pos)
        collect_indices(pos + 1)

    collect_indices(0)

    right_brackets.reverse()

    matches_found = 0
    right_pointer = 0
    right_limit = len(right_brackets)

    while right_pointer < right_limit:
        if right_pointer == right_limit:
            break
        for opening_position in left_brackets:
            if right_pointer >= right_limit:
                break
            if opening_position < right_brackets[right_pointer]:
                matches_found += 1
                right_pointer += 1
        break

    return matches_found >= 2