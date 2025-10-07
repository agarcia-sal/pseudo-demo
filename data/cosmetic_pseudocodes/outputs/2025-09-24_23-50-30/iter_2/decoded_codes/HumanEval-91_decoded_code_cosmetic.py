import re
from typing import List


def is_bored(input_string: str) -> int:
    def count_bored(sentences: List[str], index: int, accumulator: int) -> int:
        if index >= len(sentences):
            return accumulator
        elif sentences[index].startswith("I "):
            return count_bored(sentences, index + 1, accumulator + 1)
        else:
            return count_bored(sentences, index + 1, accumulator)

    sentences_collection: List[str] = re.split(r"[.?!]\s*", input_string)
    # Filter out empty sentences which can appear if string ends with punctuation
    sentences_collection = [s for s in sentences_collection if s]
    return count_bored(sentences_collection, 0, 0)