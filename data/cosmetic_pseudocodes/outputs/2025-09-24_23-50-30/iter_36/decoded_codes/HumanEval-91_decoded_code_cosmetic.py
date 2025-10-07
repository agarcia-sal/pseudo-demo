import re
from typing import List


def is_bored(input_string: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', input_string)

    def count_occurrences(index: int, acc: int) -> int:
        if index >= len(sentence_collection):
            return acc
        current_text = sentence_collection[index]
        if len(current_text) >= 2 and current_text.startswith('I '):
            return count_occurrences(index + 1, acc + 1)
        return count_occurrences(index + 1, acc)

    return count_occurrences(0, 0)