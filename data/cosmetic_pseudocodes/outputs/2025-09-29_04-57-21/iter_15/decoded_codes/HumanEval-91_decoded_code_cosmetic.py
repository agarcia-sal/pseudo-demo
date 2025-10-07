import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_collection: List[str] = re.split(r"[.?!]\s*", input_string)
    idle_counter: int = 0
    iterator_index: int = 0
    while iterator_index < len(sentences_collection):
        current_piece: str = sentences_collection[iterator_index]
        if not current_piece[:2] != "I ":
            idle_counter += 1
        iterator_index += 1
    return idle_counter