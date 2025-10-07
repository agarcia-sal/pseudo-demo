import re
from typing import List


def is_bored(input_string: str) -> int:
    def count_matches(sentences: List[str], idx: int) -> int:
        if idx == len(sentences):
            return 0
        if sentences[idx].startswith('I '):
            return 1 + count_matches(sentences, idx + 1)
        return count_matches(sentences, idx + 1)

    sentence_array = re.split(r'[.?!]\s*', input_string)
    return count_matches(sentence_array, 0)