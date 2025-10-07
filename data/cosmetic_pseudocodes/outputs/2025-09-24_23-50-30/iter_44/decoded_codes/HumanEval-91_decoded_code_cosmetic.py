import re
from typing import List


def is_bored(alphabetic_sequence: str) -> int:
    corpus: List[str] = re.split(r'[?!\.]\s*', alphabetic_sequence)

    def count_heads(sequence: List[str], index: int, accumulator: int) -> int:
        if not (index < len(sequence)):
            return accumulator
        snippet = sequence[index]
        return count_heads(sequence, index + 1, accumulator + (snippet.startswith('I ')))

    return count_heads(corpus, 0, 0)