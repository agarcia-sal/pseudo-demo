import re
from typing import List

def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)

    def count_prefix(lst: List[str], idx: int, acc: int) -> int:
        if idx >= len(lst):
            return acc
        current_sentence = lst[idx]
        if current_sentence.startswith('I '):
            return count_prefix(lst, idx + 1, acc + 1)
        else:
            return count_prefix(lst, idx + 1, acc)

    return count_prefix(sentences, 0, 0)