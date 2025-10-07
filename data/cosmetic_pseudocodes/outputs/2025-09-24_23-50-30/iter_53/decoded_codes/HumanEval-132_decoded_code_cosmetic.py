from typing import List


def is_nested(arbitrary_string: str) -> bool:
    beginnings: List[int] = []
    ends: List[int] = []
    cursor: int = 0
    length: int = len(arbitrary_string)

    while cursor < length:
        if arbitrary_string[cursor] == '[':
            beginnings.append(cursor)
        else:
            ends.append(cursor)
        cursor += 1

    rev_ends: List[int] = []
    i: int = len(ends) - 1
    while i >= 0:
        rev_ends.append(ends[i])
        i -= 1

    tally: int = 0
    pointer: int = 0
    limit: int = len(rev_ends)

    for element in beginnings:
        if pointer < limit and element < rev_ends[pointer]:
            tally += 1
            pointer += 1

    return tally >= 2