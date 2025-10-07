from typing import List


def is_nested(string: str) -> bool:
    starts: List[int] = []
    ends: List[int] = []
    for idx in range(len(string)):
        if string[idx] == '[':
            starts.append(idx)
        else:
            ends.append(idx)
    ends.reverse()
    tally = 0
    pointer = 0
    maxEnds = len(ends)
    for startIdx in starts:
        if pointer < maxEnds:
            if startIdx < ends[pointer]:
                tally += 1
                pointer += 1
    return tally >= 2