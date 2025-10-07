import re
from typing import List


def is_bored(input_string: str) -> int:
    def count_boredom(sentences_list: List[str], idx: int, acc: int) -> int:
        if idx >= len(sentences_list):
            return acc
        current_phrase = sentences_list[idx]
        if current_phrase.startswith("I "):
            return count_boredom(sentences_list, idx + 1, acc + 1)
        else:
            return count_boredom(sentences_list, idx + 1, acc)

    broken_sentences = re.split(r"[.?!]\s*", input_string)
    return count_boredom(broken_sentences, 0, 0)