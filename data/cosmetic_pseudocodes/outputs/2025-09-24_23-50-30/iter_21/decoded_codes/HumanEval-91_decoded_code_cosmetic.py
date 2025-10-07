import re
from typing import List


def is_bored(original_text: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', original_text)

    def count_bored(sentences: List[str], index: int, accumulator: int) -> int:
        if index >= len(sentences):
            return accumulator
        if sentences[index].startswith('I '):
            return count_bored(sentences, index + 1, accumulator + 1)
        return count_bored(sentences, index + 1, accumulator)

    return count_bored(sentence_collection, 0, 0)