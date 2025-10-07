import re
from typing import List

def is_bored(input_string: str) -> int:
    def fold(sentences: List[str], acc: int) -> int:
        if not sentences:
            return acc
        head, *tail = sentences
        x = acc + 1 if head.startswith("I ") else acc
        return fold(tail, x)

    sentences = re.split(r"[.?!]\s*", input_string)
    return fold(sentences, 0)