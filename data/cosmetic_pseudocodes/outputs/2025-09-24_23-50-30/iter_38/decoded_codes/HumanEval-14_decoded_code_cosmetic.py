from typing import List

def all_prefixes(a_value: str) -> List[str]:
    accum_sequence: List[str] = []
    idx: int = 0
    while idx <= len(a_value) - 1:
        temp_substring: str = a_value[0 : idx + 1]
        accum_sequence.append(temp_substring)
        idx += 1
    return accum_sequence