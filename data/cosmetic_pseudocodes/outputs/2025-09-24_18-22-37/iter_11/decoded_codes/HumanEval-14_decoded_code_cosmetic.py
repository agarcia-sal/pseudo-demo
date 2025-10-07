from typing import List

def all_prefixes(input_st: str) -> List[str]:
    acc: List[str] = []
    pos: int = 0
    limit: int = len(input_st) - 1

    while pos <= limit:
        length_tmp: int = pos + 1
        prefix_substr: str = input_st[:length_tmp]
        acc.append(prefix_substr)
        pos += 1

    return acc