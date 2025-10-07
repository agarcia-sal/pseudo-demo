import re
from typing import List


def is_bored(source_text: str) -> int:
    fragment_collection: List[str] = re.split(r'[.?!]\s*', source_text)

    def count_bored_fragments(index: int, accumulator: int) -> int:
        if index >= len(fragment_collection):
            return accumulator
        current_fragment = fragment_collection[index]
        updated_accumulator = accumulator + (
            1 if len(current_fragment) >= 2 and current_fragment[0] == 'I' and current_fragment[1] == ' ' else 0
        )
        return count_bored_fragments(index + 1, updated_accumulator)

    return count_bored_fragments(0, 0)