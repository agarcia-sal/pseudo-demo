import re
from typing import List

def is_bored(input_string: str) -> int:
    sentence_map: List[str] = re.split(r"[.?!]\s*", input_string)

    def count_prefix(sequence: List[str], index: int, accumulator: int) -> int:
        if not (index < len(sequence)):
            return accumulator
        if sequence[index].startswith("I "):
            return count_prefix(sequence, index + 1, accumulator + 1)
        else:
            return count_prefix(sequence, index + 1, accumulator)

    return count_prefix(sentence_map, 0, 0)