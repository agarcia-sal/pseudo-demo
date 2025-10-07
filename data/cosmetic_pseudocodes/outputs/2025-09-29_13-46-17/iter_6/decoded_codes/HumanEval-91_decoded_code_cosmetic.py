import re
from typing import List


def is_bored(input_string: str) -> int:
    def sub_str_check(s: str) -> bool:
        if len(s) < 2:
            return False
        return s[0] == 'I' and s[1] == ' '

    def iter_counter(sentences: List[str], idx: int, acc: int) -> int:
        if idx >= len(sentences):
            return acc
        increment = 1 if sub_str_check(sentences[idx]) else 0
        return iter_counter(sentences, idx + 1, acc + increment)

    sentences_collection = re.split(r'[.?!]\s*', input_string)
    return iter_counter(sentences_collection, 0, 0)