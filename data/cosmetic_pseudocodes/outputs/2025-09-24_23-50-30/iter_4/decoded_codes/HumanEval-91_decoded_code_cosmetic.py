import re
from typing import List


def is_bored(input_string: str) -> int:
    def count_prefix(sentences: List[str], index: int, acc: int) -> int:
        if index == len(sentences):
            return acc
        return count_prefix(
            sentences,
            index + 1,
            acc + (1 if re.match(r"^I ", sentences[index]) else 0),
        )

    parts = re.split(r"[.?!]\s*", input_string)
    return count_prefix(parts, 0, 0)